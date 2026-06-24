import os
import webbrowser

from datetime import datetime

from modules.speak import speak
from modules.logger import log_command
from modules.system_monitor import get_system_status

from modules.memory import (
    remember,
    recall,
    get_all_memories
)
def execute(command):

    command = command.lower().strip()

    log_command(command)

    # Greetings

    if "hello" in command:

        speak("Hello Vishnu")

    elif "your name" in command:

        speak("My name is Jarvis")

    # Applications

    elif "chrome" in command:

        speak("Opening Chrome")
        os.system("start chrome")

    elif "notepad" in command:

        speak("Opening Notepad")
        os.system("notepad")

    elif "visual studio code" in command or "vs code" in command:

        speak("Opening Visual Studio Code")
        os.system("code")

    # Websites

    elif "google" in command:

        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:

        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # Time

    elif "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    # Date

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
    # UNKNOWN COMMAND
    # =========================

    else:

        speak(
            "I do not know that command yet."
        )