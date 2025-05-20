import chromadb
import os
import json

qa = "data/qa_data.json"
design_decisions = "data/design_decisions.json"
chroma_client = chromadb.PersistentClient(path="./chromadb_store")
collection = chroma_client.get_or_create_collection(name="sa_chunks")

def store_chunk(chunk_text, embedding, metadata):
    chunk_id = metadata["chunk_id"]
    collection.add(
        documents=[chunk_text],
        embeddings=[embedding],
        metadatas=[metadata],
        ids=[chunk_id]
    )

def list_all_chunks():
    results = collection.get(include=["metadatas", "documents"], limit=1000)
    return [
        {
            "chunk_id": id,
            "metadata": metadata,
            "text": doc
        }
        for id, metadata, doc in zip(results["ids"], results["metadatas"], results["documents"])
    ]

def save_quality_attributes(attributes):
    os.makedirs("data", exist_ok=True)
    if os.path.exists(qa):
        with open(qa, "r") as f:
            data = json.load(f)
    else:
        data = {}
    data_new = json.loads(attributes)
    data.extend(data_new)
    with open(qa, "w") as f:
        json.dump(data, f, indent=2)

def save_design_decisions(decisions):
    os.makedirs("data", exist_ok=True)
    if os.path.exists(design_decisions):
        with open(design_decisions, "r") as f:
            data = json.load(f)
    else:
        data = {}
    data_new = json.loads(decisions)
    data.extend(data_new)
    with open(design_decisions, "w") as f:
        json.dump(data, f, indent=2)
