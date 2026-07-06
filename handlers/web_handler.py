"""
Website Handler

Handles all website opening commands.
"""

import webbrowser

from modules.speak import speak


def handle_web(command):
    """
    Executes website related commands.

    Returns
    -------
    bool
        True if handled.
        False otherwise.
    """

    if "google" in command:

        speak("Opening Google")

        webbrowser.open("https://www.google.com")

        return True

    elif "youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://www.youtube.com")

        return True

    elif "github" in command:

        speak("Opening GitHub")

        webbrowser.open("https://github.com")

        return True

    elif "chatgpt" in command:

        speak("Opening ChatGPT")

        webbrowser.open("https://chat.openai.com")

        return True

    elif "linkedin" in command:

        speak("Opening LinkedIn")

        webbrowser.open("https://linkedin.com")

        return True

    return False