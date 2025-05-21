from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("GOOGLE_AI_API_KEY")
from google.genai import types

client = genai.Client(api_key=api_key)

input_text = input("Haz tu pregunta: ")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[input_text],
    config=types.GenerateContentConfig(
        max_output_tokens=500,
        temperature=0.95
    )
)
print(response.text)