"""
System Handler

Handles all system monitoring commands.
"""

from modules.speak import speak
from modules.system_monitor import get_system_status


def handle_system(command):
    """
    Executes system related commands.

    Returns
    -------
    bool
        True if handled.
        False otherwise.
    """

    if "system status" in command:

        cpu, ram, disk = get_system_status()

        speak(
            f"CPU usage is {cpu} percent. "
            f"RAM usage is {ram} percent. "
            f"Disk usage is {disk} percent."
        )

        return True

    return False