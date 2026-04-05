import sys
import os
import time
import datetime
from speech_module import speak, listen
from brain import get_ai_response

def wish_me():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning sir.")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir.")
    else:
        speak("Good Evening sir.")
    speak("I am Jarvis. How can I help you today?")

def run_jarvis():
    wish_me()
    
    # Default to voice mode, but switch to text if passed via terminal flag
    mode = 'v'
    if len(sys.argv) > 1 and sys.argv[1] in ['--text', '-t']:
        mode = 't'
        speak("Text Mode activated. I am ready for your keyboard commands.")
    else:
        speak("Voice Mode activated. I am listening for your commands.")
        
    speak("I am fully operational.")

    while True:
        if mode == 'v':
            # Listen for the wake word continuously but silently loop unless error
            query = listen(timeout=None, phrase_time_limit=5)
            
            if query == "error":
                time.sleep(2)
                continue
                
            if 'jarvis' not in query and 'exit' not in query and 'shut down' not in query:
                continue
            
            if 'jarvis' in query:
                speak("Yes sir?")
                command = listen(timeout=10, phrase_time_limit=15)
            else:
                command = query # it was exit or shutdown
                
            if command == 'none' or command == 'error':
                continue
                
        else:
            # Text Mode
            command = input("\nYou: ").strip().lower()
            if not command:
                continue
        
        # Phase 2: Process the command, regardless of text or voice input
        if 'exit' in command or 'shut down' in command or 'goodbye' in command:
            speak("Shutting down systems. Goodbye sir.")
            sys.exit()
        elif 'open chrome' in command:
            speak("Ok sir, opening Chrome.")
            os.system("start chrome")
        elif 'open vs code' in command or 'open code' in command:
            speak("Ok sir, opening Visual Studio Code.")
            os.system("code")
        elif 'open notepad' in command:
            speak("Ok sir, opening Notepad.")
            os.system("notepad")
        elif 'open command prompt' in command or 'open cmd' in command:
            speak("Ok sir, opening Command Prompt.")
            os.system("start cmd")
        elif 'open file explorer' in command or 'open folder' in command:
            speak("Ok sir, opening File Explorer.")
            os.system("explorer")
        else:
            response = get_ai_response(command)
            speak(response)

if __name__ == "__main__":
    run_jarvis()
