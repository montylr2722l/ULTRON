"""
Utility Handler

Handles greetings, time, date and exit commands.
"""

from datetime import datetime

from modules.speak import speak
from config import USER_NAME, APP_NAME


def handle_utility(command):

    # =========================
    # Greetings
    # =========================

    if "hello" in command:

        speak(f"Hello {USER_NAME}")
        return True

    if "your name" in command:

        speak(f"My name is {APP_NAME}")
        return True

    # =========================
    # Time
    # =========================

    if "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        speak(f"The time is {current_time}")

        return True

    # =========================
    # Date
    # =========================

    if "date" in command:

        current_date = datetime.now().strftime("%d %B %Y")

        speak(f"Today's date is {current_date}")

        return True

    # =========================
    # Exit
    # =========================

    if any(
        word in command
        for word in (
            "exit",
            "close",
            "shutdown",
            "stop"
        )
    ):

        speak(f"Goodbye {USER_NAME}")

        return "exit"

    return False