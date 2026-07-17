"""
Local AI Brain

Handles AI conversations using Ollama.
"""

import ollama

from config import AI_MODEL

from modules.conversation import (
    get_history,
    add_user_message,
    add_ai_message
)


def ask_ai(prompt):
    """
    Sends the complete conversation to Ollama.
    """

    try:

        # Save user message
        add_user_message(prompt)

        # Get full conversation
        history = get_history()

        response = ollama.chat(

            model=AI_MODEL,

            messages=history

        )

        answer = response["message"]["content"]

        # Save AI reply
        add_ai_message(answer)

        return answer

    except Exception as e:

        return f"AI Error: {e}"