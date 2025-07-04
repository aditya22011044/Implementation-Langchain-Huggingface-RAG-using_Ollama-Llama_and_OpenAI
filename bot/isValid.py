import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print(response)
except openai.AuthenticationError as e:
    print(f"Authentication Error: {e}")
