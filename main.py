"""
Main entry point for ULTRON.
Handles both Voice and Text interaction.
"""

import time

from config import CONVERSATION_TIMEOUT ,APP_NAME, USER_NAME
from modules.listen import listen
from modules.speak import speak
from modules.greet import greet
from modules.conversation import initialize_conversation
from commands import execute


def main():
    initialize_conversation()
    greet()

    conversation_mode = False
    last_activity = 0

    while True:

        print("\n================================")
        print("Press ENTER for Voice Command")
        print("Or type a command directly")
        print("================================")

        text_input = input("You: ").strip().lower()

        # ==========================
        # TEXT MODE
        # ==========================

        if text_input:

            if text_input == APP_NAME.lower():

                speak(f"Yes {USER_NAME}")

                conversation_mode = True
                last_activity = time.time()

                continue

            result = execute(text_input)

            if result == "exit":
                break

            continue

        # ==========================
        # VOICE MODE
        # ==========================

        if conversation_mode:

            command = listen()

            if command:

                last_activity = time.time()

                result = execute(command)

                if result == "exit":
                    break

            if time.time() - last_activity > CONVERSATION_TIMEOUT:

                conversation_mode = False

                speak("Standing by")

        else:

            wake_word = listen()

            if wake_word:

                if APP_NAME.lower() in wake_word:

                    speak("Yes Vishnu")

                    conversation_mode = True

                    last_activity = time.time()


if __name__ == "__main__":
    main()