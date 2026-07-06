"""
Local AI Brain

Uses Ollama to answer unknown commands.
"""

import ollama

from config import AI_MODEL


def ask_ai(prompt):

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

        return f"AI Error: {e}"