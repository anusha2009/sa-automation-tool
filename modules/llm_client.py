import requests

def query_llm(prompt, model="llama3.1:8b"):
    api_url = "https://nebula.cs.vu.nl/api/chat/completions"
    
    headers = {
        'Authorization': f'Bearer {'sk-3a943a51b6b944f9865bab3634bf2cf8'}',
        'Content-Type': 'application/json'
    }
    payload = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "model": model,
        "stream": False
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"[LLM Error]: {e}"
