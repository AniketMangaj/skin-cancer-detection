import requests
import json

GEMINI_API_KEY = "AIzaSyBYHbOJyng-5j_Xc3TDc1UckKE7aSzR3Qo"
MODEL_NAME = "gemini-1.5-flash-latest"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent"

def call_gemini_api(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return "Error: API key missing"

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY
    }

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        print(json.dumps(data, indent=2))  # <-- Log the entire response for debugging

        if 'candidates' in data and data['candidates']:
            return data['candidates'][0]['content']['parts'][0]['text']
        return "No candidates found."

    except Exception as e:
        return f"Error: {str(e)}"

# Test it
print(call_gemini_api("What is skin cancer?"))
