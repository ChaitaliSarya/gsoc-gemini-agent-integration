# gemini_provider.py
# This class wraps the Gemini API calls

from google import generativeai as genai

class GeminiProvider:
    """
    GeminiProvider class to handle API calls to Gemini models.
    """

    def __init__(self, api_key: str, model_name='gemini-pro'):
        # Configure the SDK with your API key
        genai.configure(api_key=api_key)
        # Choose which model to use
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt: str) -> str:
        """
        Generates text from Gemini based on the input prompt.
        Returns the generated text.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text if response else 'No response'
        except Exception as e:
            # Handle API errors
            return f'Error: {str(e)}'
