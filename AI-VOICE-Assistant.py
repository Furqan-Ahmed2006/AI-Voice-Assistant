import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()
engine=pyttsx3.init()
engine.setProperty("rate",180)
api_key=os.getenv("OPENROUTER_API_KEY")
def speak(text):
    engine.say(text)
    engine.runAndWait()
def generate_ai_response(prompt):
    """Get AI response from OpenRouter"""
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={ 
                "model": "google/gemini-3-flash-preview",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 300 
            }
        )
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return f"API Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"AI Error: {e}"
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    else:
        response=generate_ai_response(c)
        speak(response)
        print("Jarvis:",response)
speak("Initializing Jarvis----")
while True:
    r=sr.Recognizer()
    print("Recognizing-----")
    try:
        with sr.Microphone(device_index=0) as source:
            r.adjust_for_ambient_noise(source, duration=1) 
            print("Listening----")
            audio=r.listen(source,timeout=2,phrase_time_limit=2)
        command=r.recognize_google(audio)
        print("You said:",command)
        if (command.lower().strip()=="jarvis"):
            speak("Yes Sir! How can I help you---")
            with sr.Microphone(device_index=0) as source:
                r.adjust_for_ambient_noise(source, duration=1) 
                print("Jarvis Active----Listening for Command----")
                audio=r.listen(source,timeout=5,phrase_time_limit=5)
                command=r.recognize_google(audio)
                print("Command:",command)
                processcommand(command)
    except Exception as e:
        print("Error:",e)
        continue
