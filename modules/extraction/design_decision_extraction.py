from modules.prompts import design_decision_extraction_prompt_2
from modules.llm_client import query_llm
from modules.query_engine import retrieve_relevant_chunks, construct_prompt
from modules.storage import save_design_decisions
import json

def extract_design_decisions() -> list[str]:
    context_chunks = retrieve_relevant_chunks("Identify architectural design decisions, including rationale and any considered alternatives")
    prompt = design_decision_extraction_prompt_2.format()
    final_prompt = construct_prompt(prompt, context_chunks)
    response = query_llm(final_prompt)
    try:
        start = response.find("[")
        end = response.rfind("]") + 1
        json_result = response[start:end]
        result = json.loads(json_result)
        save_design_decisions(json.dumps(result))
        return result

    except Exception as e:
        return {"error": str(e), "raw_response": response}

    return result

