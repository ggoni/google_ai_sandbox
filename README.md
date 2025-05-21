# Google AI Gemini API Text Generation

A simple Python script that demonstrates how to use the Google AI Gemini API for text generation with customizable temperature settings.

## Features

- Text generation using Google's Gemini 2.0 Flash model
- Environment variable support for API key management
- Interactive command-line interface
- Configurable temperature settings for response creativity

## Prerequisites

- Python 3.x
- Google AI API key (get one from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation

1. Clone this repository:
```bash
git clone https://github.com/ggoni/google_ai_sandbox
cd google_ai_sandbox
```

2. Install the required packages:
```bash
pip install google-generativeai python-dotenv
```

3. Create a `.env` file in the project root and add your API key:
```
GOOGLE_AI_API_KEY=your_api_key_here
```

## Usage

1. Run the script:
```bash
python main.py
```

2. Enter your question when prompted
3. The script will generate a response using the Gemini model

## Code Example

```python
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_AI_API_KEY")

# Initialize client
client = genai.Client(api_key=api_key)

# Generate content
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Your question here"
)
print(response.text)
```

## API Documentation

For more information about the Google AI Gemini API, visit:
- [Google AI Gemini API Documentation](https://ai.google.dev/gemini-api/docs/text-generation)

## Security

- Never commit your `.env` file or expose your API key
- Add `.env` to your `.gitignore` file
- Keep your API key secure and rotate it if compromised

## License

This project is licensed under the MIT License - see the LICENSE file for details.
