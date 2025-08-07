import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_command(user_input):
    prompt = f"""
You are an assistant that converts natural language into safe Windows terminal commands.
Do not add explanations. Only return the Windows command.

Input: {user_input}
Output:
"""
    response = model.generate_content(prompt)
    return response.text.strip()
