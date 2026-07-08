"""
Prompt Builder

Builds the complete prompt for the AI by
combining system prompt, long-term memory,
conversation history and the current query.
"""

from modules.memory import get_all_memories


def build_system_prompt():

    prompt = (
        "You are JARVIS, a professional offline AI assistant.\n"
        "You are intelligent, concise, friendly and helpful.\n"
        "Always answer naturally.\n"
    )

    memories = get_all_memories()

    if memories:

        prompt += "\nKnown User Information:\n"

        for key, value in memories.items():

            prompt += f"- {key}: {value}\n"

    return prompt