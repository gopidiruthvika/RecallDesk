import os
from dotenv import load_dotenv
from groq import Groq

# Load variables from .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("ERROR: Groq API key not found in .env")
    exit()

# Connect to Groq
client = Groq(api_key=api_key)

# Send a simple request
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Say hello to RecallDesk in one short sentence."
        }
    ]
)

print(response.choices[0].message.content)