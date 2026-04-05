import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY and API_KEY != "INSERT_YOUR_GEMINI_API_KEY_HERE":
    genai.configure(api_key=API_KEY)
    # Using gemini-1.5-flash for speed
    model = genai.GenerativeModel('gemini-1.5-flash',
        system_instruction="You are Jarvis, a highly intelligent AI assistant mimicking Iron Man's Jarvis. You are helping your creator. Keep responses EXTREMELY concise and spoken-word friendly. No markdown, no code blocks, no asterisks. Reply in one to two short sentences maximum.")
    chat = model.start_chat()
else:
    model = None
    chat = None

def get_ai_response(user_input):
    if not chat:
        return "I am currently disconnected from my brain because the Gemini API key is missing from the dot env file."
    try:
        response = chat.send_message(user_input)
        return response.text.replace('*', '').replace('#', '')  # clean up any stray markdown
    except Exception as e:
        print(f"AI Error: {e}")
        return "I'm sorry, I'm having trouble processing that right now."
