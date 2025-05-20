
from modules.prompts import tradeoff_prompt
from modules.llm_client import query_llm
from modules.query_engine import retrieve_relevant_chunks, construct_prompt
import json

def extract_tradeoffs() -> list[str]:
    context_chunks = retrieve_relevant_chunks("architectural design decisions")
    prompt = tradeoff_prompt.format()
    final_prompt = construct_prompt(prompt, context_chunks)
    response = query_llm(final_prompt)
    return response

