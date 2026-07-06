"""
Command Router

Receives commands and forwards them to the appropriate handler.
"""

from datetime import datetime

from modules.speak import speak
from modules.logger import log_command
from modules.ai_brain import ask_ai

from handlers.app_handler import handle_app
from handlers.web_handler import handle_web
from handlers.memory_handler import handle_memory
from handlers.system_handler import handle_system


def execute(command):

    command = command.lower().strip()

    log_command(command)

    # =========================
    # GREETINGS
    # =========================

    if "hello" in command:

        speak("Hello Vishnu")
        return

    elif "your name" in command:

        speak("My name is Jarvis")
        return

    # =========================
    # APPLICATION HANDLER
    # =========================

    if handle_app(command):
        return

    # =========================
    # WEBSITE HANDLER
    # =========================

    if handle_web(command):
        return

    # =========================
    # MEMORY HANDLER
    # =========================

    if handle_memory(command):
        return

    # =========================
    # TIME
    # =========================

    if "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        speak(f"The time is {current_time}")
        return

    # =========================
    # DATE
    # =========================

    if "date" in command:

        current_date = datetime.now().strftime("%d %B %Y")

        speak(f"Today's date is {current_date}")
        return
    # =========================
    # SYSTEM HANDLER
    # =========================

    if handle_system(command):
     return
    # =========================
    # EXIT
    # =========================

    if any(
        word in command
        for word in [
            "exit",
            "close",
            "shutdown",
            "stop"
        ]
    ):

        speak("Goodbye Vishnu")

        return "exit"

    # =========================
    # AI FALLBACK
    # =========================

    try:

        speak("Thinking")

        response = ask_ai(command)

        print("\n==============================")
        print("AI Response")
        print("==============================")
        print(response)

        speak(response[:300])

    except Exception as e:

        print("AI Error:", e)

        speak(
            "Sorry Vishnu, my AI brain is currently unavailable."
        )