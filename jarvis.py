import speech_recognition as sr
import pyttsx3
import webbrowser
from music import music 
from openai import OpenAI

r = sr.Recognizer()
engine = pyttsx3.init()       
#      = pyttsx3.Engine()
# This init() function returns Engine class which makes our engine variable an object so we can use 'say' and 'run' methods

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ai(c):
    client = OpenAI(api_key="Put_Your_Key_here")

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis and skilled in general tasks like Alexa but keep your responses short"},
        {"role": "user", "content": c}
    ]
)
    return (completion.choices[0].message.content)

def execute(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkden.com")

    elif "play jagjit singh" in c.lower():
        webbrowser.open(music['jagjit singh'])
    elif "play classic" in c.lower():
        webbrowser.open(music['classic'])
    elif "play honey singh" in c.lower() or "play hani singh" in c.lower():
        webbrowser.open(music['honey singh'])
    elif "play english" in c.lower():
        webbrowser.open(music['english'])

    else: 
         answer = ai(c)
         speak(answer)

if __name__== '__main__':
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                print('Listening...')
                audio = r.listen(source)

            word = r.recognize_google(audio)                            # type: ignore
            if word.lower() == 'jarvis':
                speak('Ya')

                with sr.Microphone() as source:
                    print('Jarvis Active...')
                    audio = r.listen(source)

                command = r.recognize_google(audio)                     # type: ignore
                if command in ['stop', 'exit']:
                    break

                execute(command)
        
        except Exception as e:
            print(f"Sphinx error; {e}")