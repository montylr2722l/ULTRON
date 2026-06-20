from modules.listen import listen
from modules.speak import speak
from modules.commands import execute
from modules.greet import greet

import time

greet()

conversation_mode = False
last_activity = 0

while True:

    if conversation_mode:

        command = listen()

        if command:

            last_activity = time.time()

            if "exit" in command:
                speak("Goodbye Vishnu")
                break

            execute(command)

        if time.time() - last_activity > 30:

            conversation_mode = False

            speak("Standing by")

    else:

        wake_word = listen()

        if "exit" in wake_word:

            speak("Goodbye Vishnu")
            break

        if "jarvis" in wake_word:

            speak("Yes Vishnu")

            conversation_mode = True

            last_activity = time.time()