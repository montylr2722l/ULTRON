from modules.speak import speak
from modules.ai_brain import ask_ai


def handle_ai(command):

    try:

        speak("Thinking")

        response = ask_ai(command)

        speak(response[:300])

    except Exception as e:

        print("AI Error:", e)

        speak("Sorry Vishnu, my AI brain is currently unavailable.")

    return True