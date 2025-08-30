# test_provider.py
# Test GeminiProvider functionality

import sys, os

# Add src folder to Python path so we can import GeminiProvider
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from gemini_provider import GeminiProvider

def test_dummy():
    # Test that GeminiProvider can be initialized
    provider = GeminiProvider(api_key='TEST_KEY')
    assert provider is not None
