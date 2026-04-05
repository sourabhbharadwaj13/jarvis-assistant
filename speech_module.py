import pyttsx3
import speech_recognition as sr

def init_engine():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # Try to find a male voice for Jarvis or just use the default
    for voice in voices:
        if 'david' in voice.name.lower():  # Standard MS David voice is masculine
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 170)
    return engine

engine = init_engine()

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen(timeout=5, phrase_time_limit=10):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Calibrating microphone for background noise... Please wait.")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        r.pause_threshold = 1.0 # Wait 1 second before considering speech ended
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-US')
            print(f"User said: {query}\n")
            return query.lower()
        except sr.WaitTimeoutError:
            print("[Debug] Timed out waiting for you to speak.")
            return "none"
        except sr.UnknownValueError:
            print("[Debug] I heard you, but couldn't understand what you said.")
            return "none"
        except sr.RequestError:
            print("Error connecting to Google Speech Recognition service.")
            return "error"
        except Exception as e:
            print(f"Error during listening: {e}")
            return "error"
