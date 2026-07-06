"""
Application Handler

Handles all desktop application commands.
"""

import os

from modules.speak import speak


def handle_app(command):
    """
    Executes application related commands.

    Returns
    -------
    bool
        True if command handled.
        False otherwise.
    """

    if "chrome" in command:

        speak("Opening Chrome")

        os.system("start chrome")

        return True

    elif "notepad" in command:

        speak("Opening Notepad")

        os.system("notepad")

        return True

    elif "visual studio code" in command or "vs code" in command:

        speak("Opening Visual Studio Code")

        os.system("code")

        return True

    return False