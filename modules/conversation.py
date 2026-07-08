"""
Conversation Manager

Maintains the current chat history for the AI.
"""

MAX_HISTORY = 20
history = []


def initialize_conversation():
    """
    Starts a fresh conversation.
    """

    global history

    history = [
        {
            "role": "system",
            "content": (
                "You are JARVIS, a professional offline AI assistant. "
                "You are helpful, intelligent, concise and friendly. "
                "Answer clearly and remember the current conversation."
            )
        }
    ]


def get_history():
    """
    Returns the current conversation history.
    """

    return history


def add_user_message(message):
    """
    Adds a user message.
    """

    history.append(
        {
            "role": "user",
            "content": message
        }
    )

    trim_history()

def add_ai_message(message):
    """
    Adds an AI response.
    """

    history.append(
        {
            "role": "assistant",
            "content": message
        }
    )

    trim_history()

def clear_history():
    """
    Clears the conversation.
    """

    initialize_conversation()


def trim_history():
    """
    Keeps only the latest conversation.

    System prompt is always preserved.
    """

    global history

    system_prompt = history[0]

    recent_messages = history[-MAX_HISTORY:]

    history = [system_prompt] + recent_messages    
    