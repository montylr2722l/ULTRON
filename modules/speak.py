"""
Text To Speech Module
"""

import pyttsx3

from config import (
    VOICE_RATE,
    VOICE_VOLUME
)

engine = pyttsx3.init()

engine.setProperty("rate", VOICE_RATE)

engine.setProperty("volume", VOICE_VOLUME)

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)


def speak(text):

    print(f"Jarvis: {text}")

    engine.say(text)

    engine.runAndWait()