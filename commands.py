import os
import webbrowser

from datetime import datetime
from handlers.app_handler import handle_app
from handlers.web_handler import handle_web
from modules.speak import speak
from modules.logger import log_command
from modules.system_monitor import get_system_status
from modules.ai_brain import ask_ai

from modules.memory import (
    remember,
    recall,
    get_all_memories
)


def execute(command):

    command = command.lower().strip()

    log_command(command)

    # =========================
    # GREETINGS
    # =========================

    if "hello" in command:

        speak("Hello Vishnu")

    elif "your name" in command:

        speak("My name is Jarvis")

    # =========================
    # APPLICATIONS
    # =========================
    
    if handle_app(command):

     return
    
    # =========================
    # WEBSITES
    # =========================
    if handle_web(command):

     return
    # =========================
    # TIME
    # =========================

    elif "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        speak(f"The time is {current_time}")

    # =========================
    # DATE
    # =========================

    elif "date" in command:

        current_date = datetime.now().strftime("%d %B %Y")

        speak(f"Today's date is {current_date}")

    # =========================
    # SMART MEMORY ENGINE
    # =========================

    elif command.startswith("remember my"):

        content = command.replace(
            "remember my",
            "",
            1
        ).strip()

        if " is " in content:

            key, value = content.split(
                " is ",
                1
            )

            key = key.strip()
            value = value.strip()

            remember(key, value)

            speak(
                f"I will remember that your {key} is {value}"
            )

        else:

            speak(
                "Please use format. Remember my college is JECRC"
            )

    elif command.startswith("what is my"):

        key = command.replace(
            "what is my",
            "",
            1
        ).strip()

        value = recall(key)

        if value:

            speak(
                f"Your {key} is {value}"
            )

        else:

            speak(
                f"I do not know your {key} yet"
            )

    elif "show all memories" in command:

        memories = get_all_memories()

        if memories:

            response = "I remember "

            for key, value in memories.items():

                response += (
                    f"your {key} is {value}. "
                )

            speak(response)

        else:

            speak(
                "I do not remember anything yet."
            )

    # =========================
    # SYSTEM STATUS
    # =========================

    elif "system status" in command:

        cpu, ram, disk = get_system_status()

        speak(
            f"CPU usage is {cpu} percent. "
            f"RAM usage is {ram} percent. "
            f"Disk usage is {disk} percent."
        )

    # =========================
    # EXIT
    # =========================

    elif any(
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

    else:

        try:

            speak("Thinking")

            response = ask_ai(command)

            print("\nAI Response:\n")
            print(response)

            speak(response[:300])

        except Exception as e:

            print("AI Error:", e)

            speak(
                "Sorry Vishnu, my AI brain is currently unavailable."
            )