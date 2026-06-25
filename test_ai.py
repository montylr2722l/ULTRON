from modules.ai_brain import ask_ai

while True:

    query = input("You: ")

    if query.lower() == "exit":
        break

    print("\nJarvis:")

    print(ask_ai(query))

    print()