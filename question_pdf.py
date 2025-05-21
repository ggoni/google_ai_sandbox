import PyPDF2
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("GOOGLE_AI_API_KEY")

# Initialize the client
client = genai.Client(api_key=api_key)

input_text = input("Haz tu pregunta: ")

# Read the PDF file
pdf_file = open('api_docs.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract text from PDF
pdf_text = ""
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    pdf_text += page.extract_text()

# Close the file
pdf_file.close()

context = [
    # The PDF text is your first piece of context
    {"text": pdf_text},
    
    # You can add additional context as needed
    {"text": input_text},
    
    # Your prompt/question is the final part
    {"text": "Just answer with the text of the api call"}
]



# Generate content using the PDF text as context
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=context
)

print(response.text)