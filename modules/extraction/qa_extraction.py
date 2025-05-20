from modules.prompts import qa_extraction_prompt, qa_extraction_prompt_5
from modules.llm_client import query_llm
from modules.query_engine import retrieve_relevant_chunks, construct_prompt
from modules.storage import save_quality_attributes
import json

def extract_quality_attributes() -> list[str]:
    context_chunks = retrieve_relevant_chunks("quality attributes,  non-functional requirements")
    prompt = qa_extraction_prompt_5.format()
    final_prompt = construct_prompt(prompt, context_chunks)
    response = query_llm(final_prompt)

    try:
        start = response.find("[")
        end = response.rfind("]") + 1
        json_result = response[start:end]
        result = json.loads(json_result)
        save_quality_attributes(json.dumps(result)) 
        return result

    except Exception as e:
        return {"error": str(e), "raw_response": response}

    return result