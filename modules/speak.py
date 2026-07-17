import pyttsx3

from config import APP_NAME 

engine = pyttsx3.init()

engine.setProperty("rate", 180)

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)


def speak(text):

    print(f"{APP_NAME}: {text}")

    engine.say(text)

    engine.runAndWait()