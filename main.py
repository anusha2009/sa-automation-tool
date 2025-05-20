from fastapi import FastAPI, UploadFile, File
from modules.ingestion import parse_document, chunk_text
from modules.embeddings import embed_text
from modules.storage import store_chunk
from modules.storage import list_all_chunks
import uuid
import os
from pydantic import BaseModel
from modules.query_engine import retrieve_relevant_chunks, construct_prompt
from modules.extraction.qa_extraction import extract_quality_attributes
from modules.extraction.design_decision_extraction import extract_design_decisions
from modules.extraction.tradeoff_analysis import extract_tradeoffs
from fastapi import APIRouter, HTTPException
from typing import Dict

app = FastAPI()

@app.post("/sis")
def calculate_sis(dmatrix, qa):
    try:
        sis_scores = {}
        for option, dimension in dmatrix["dmatrices"].items():
            sis_score = 0
            for dimension, matrix in dimension.items():
                for source, targets in matrix.items():
                    for target, impact in targets.items():
                        if impact == "-" or target not in qa:
                            continue
                        try:
                            impact = int(impact)
                            weight = qa[target]
                            sis_score += impact * weight
                        except ValueError:
                            continue
            sis_scores[option] = sis_score
        return {"sis_scores": sis_scores}
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    save_path = f"uploaded_docs/{file.filename}"
    with open(save_path, "wb") as f:
        f.write(await file.read())

    text = parse_document(save_path)
    chunks = chunk_text(text)

    for idx, chunk in enumerate(chunks):
        embedding = embed_text(chunk)
        metadata = {"chunk_id": str(uuid.uuid4()), "source_doc": file.filename, "chunk_idx": idx}
        store_chunk(chunk, embedding, metadata)

    return {"message": f"{file.filename} parsed and stored", "chunks": len(chunks)}

@app.get("/list-chunks")
def list_chunks():
    return list_all_chunks()

@app.post("/extract/qa")
def extract_qa(input: dict):
    return {"quality_attributes": extract_quality_attributes()}

@app.post("/extract/decisions")
def extract_design_decision(input: dict):
    return {"design_decisions": extract_design_decisions()}

@app.post("/extract/tradeoff")
def extract_tradeoffs(input: dict):
    return {"tradeoffs": extract_tradeoffs()}
