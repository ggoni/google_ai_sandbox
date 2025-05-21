from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("GOOGLE_AI_API_KEY")

input_text = input("Haz tu pregunta: ")

if not api_key:
    raise ValueError("GOOGLE_AI_API_KEY not found in environment variables")

# Initialize client
client = genai.Client(api_key=api_key)

# Generate content with temperature setting
response = client.models.generate_content(model="gemini-2.0-flash", contents=input_text)
print(response.text)
