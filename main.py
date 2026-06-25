from modules.listen import listen
from modules.speak import speak
from modules.commands import execute
from modules.greet import greet

import time

CONVERSATION_TIMEOUT = 30

greet()

conversation_mode = False
last_activity = 0

while True:

    print("\n================================")
    print("Press ENTER for Voice Command")
    print("Or type a command directly")
    print("================================")

    text_input = input("You: ").strip().lower()

    # =========================
    # TEXT MODE
    # =========================

    if text_input:

        if text_input == "jarvis":

            speak("Yes Vishnu")

            conversation_mode = True
            last_activity = time.time()

            continue

        result = execute(text_input)

        if result == "exit":

            break

        continue

    # =========================
    # VOICE CONVERSATION MODE
    # =========================

    if conversation_mode:

        command = listen()

        if command:

            last_activity = time.time()

            result = execute(command)

            if result == "exit":

                break

        # timeout check

        if time.time() - last_activity > CONVERSATION_TIMEOUT:

            conversation_mode = False

            speak("Standing by")

    # =========================
    # WAKE WORD MODE
    # =========================

    else:

        wake_word = listen()

        if wake_word:

            wake_word = wake_word.lower()

            # direct exit support

            if any(
                word in wake_word
                for word in [
                    "exit",
                    "close",
                    "shutdown",
                    "stop"
                ]
            ):

                speak("Goodbye Vishnu")

                break

            # wake word

            if "jarvis" in wake_word:

                speak("Yes Vishnu")

                conversation_mode = True

                last_activity = time.time()