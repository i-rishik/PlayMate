import google.generativeai as genai
import os

# Initialize Google Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

def ai_response(prompt):
    response = model.generate_content(prompt)
    return response.text