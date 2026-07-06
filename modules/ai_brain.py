"""
AI Brain Module for JARVIS.

Purpose:
Handles communication with the local Ollama AI model.
"""

import ollama

from config import AI_MODEL


def ask_ai(prompt):
    """
    Sends a prompt to the local AI model and returns its response.

    Args:
        prompt (str): User input.

    Returns:
        str: AI response.
    """

    try:

        response = ollama.chat(

            model=AI_MODEL,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response["message"]["content"]

    except Exception as e:

        return (
            "Sorry, I couldn't reach the AI model.\n"
            f"Error: {e}"
        )