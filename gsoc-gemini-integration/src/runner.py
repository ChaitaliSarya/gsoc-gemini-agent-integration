from google import generativeai as genai

# Configure your API key
api_key = "AIzaSyC4jj2KV98THJIOMsOs1n56TPDaf6ROhJw"
genai.configure(api_key=api_key)

# List available models
models = genai.list_models()
print("Available models:", models)
