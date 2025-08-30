# test_genai.py
# Test Google GenAI SDK import

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import google.generativeai as genai

def test_sdk_import():
    # Check if the SDK is imported correctly
    assert genai is not None
