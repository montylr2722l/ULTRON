"""
Greeting module for JARVIS.
"""

from datetime import datetime

from config import APP_NAME, USER_NAME
from modules.speak import speak


def greet():
    """
    Greets the user based on the current time.
    """

    hour = datetime.now().hour

    if hour < 12:
        speak(f"Good Morning {USER_NAME}")

    elif hour < 18:
        speak(f"Good Afternoon {USER_NAME}")

    else:
        speak(f"Good Evening {USER_NAME}")

    speak(f"{APP_NAME} is online.")