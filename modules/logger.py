"""
Logger module for JARVIS.

Purpose:
Logs every command executed by the user.
"""

import os

from datetime import datetime
from config import LOG_FILE


def log_command(command):
    """
    Saves a command into the log file with timestamp.
    """

    try:

        # Create logs folder if it doesn't exist
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(LOG_FILE, "a", encoding="utf-8") as file:

            file.write(f"[{current_time}] {command}\n")

    except Exception as e:

        print(f"Logger Error: {e}")