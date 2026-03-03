import os
import requests
from dotenv import load_dotenv

# Load your .env file
load_dotenv()

def list_groq_models():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ Error: GROQ_API_KEY not found in environment.")
        return

    url = "https://api.groq.com/openai/v1/models"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        models = response.json().get('data', [])
        
        print(f"{'MODEL ID':<40} | {'OWNED BY':<15}")
        print("-" * 60)
        for model in models:
            print(f"{model['id']:<40} | {model['owned_by']:<15}")
            
    except requests.exceptions.HTTPError as e:
        print(f"❌ API Error: {e.response.json().get('error', {}).get('message', 'Unknown error')}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    list_groq_models()