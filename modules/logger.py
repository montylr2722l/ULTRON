"""
Command Logger

Stores every executed command with timestamp.
"""

from datetime import datetime

from config import LOG_FILE


def log_command(command):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:

        file.write(f"[{timestamp}] {command}\n")