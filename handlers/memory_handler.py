"""
Memory Handler

Handles all memory related commands.
"""

from modules.speak import speak
from modules.memory import (
    remember,
    recall,
    get_all_memories
)


def handle_memory(command):
    """
    Executes memory related commands.

    Returns
    -------
    bool
        True if command handled.
        False otherwise.
    """

    # Remember

    if command.startswith("remember my"):

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
                "Please say something like: Remember my college is JECRC"
            )

        return True

    # Recall

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
                f"I do not know your {key} yet."
            )

        return True

    # Show all memories

    elif "show all memories" in command:

        memories = get_all_memories()

        if memories:

            response = "I remember "

            for key, value in memories.items():

                response += f"your {key} is {value}. "

            speak(response)

        else:

            speak(
                "I do not remember anything yet."
            )

        return True

    return False