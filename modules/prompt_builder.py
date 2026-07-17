"""
Prompt Builder

Builds the system prompt for the AI.
"""

from modules.memory import get_all_memories


PROMPT_FILE = "prompts/system_prompt.txt"


def build_system_prompt():

    with open(PROMPT_FILE, "r", encoding="utf-8") as file:
        prompt = file.read()

    memories = get_all_memories()

    if memories:

        prompt += "\n\nKnown User Information:\n"

        for key, value in memories.items():

          prompt += f"• {key}: {value}\n"

    return prompt