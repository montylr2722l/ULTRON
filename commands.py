"""
Command Router

Receives commands and forwards them to the appropriate handler.
"""

from modules.logger import log_command

from handlers.utility_handler import handle_utility
from handlers.app_handler import handle_app
from handlers.web_handler import handle_web
from handlers.memory_handler import handle_memory
from handlers.system_handler import handle_system
from handlers.ai_handler import handle_ai


def execute(command):

    command = command.lower().strip()

    log_command(command)

    # =========================
    # UTILITY HANDLER
    # =========================

    result = handle_utility(command)

    if result == "exit":
        return "exit"

    if result:
        return

    # =========================
    # APPLICATION HANDLER
    # =========================

    if handle_app(command):
        return

    # =========================
    # WEBSITE HANDLER
    # =========================

    if handle_web(command):
        return

    # =========================
    # MEMORY HANDLER
    # =========================

    if handle_memory(command):
        return

    # =========================
    # SYSTEM HANDLER
    # =========================

    if handle_system(command):
        return

    # =========================
    # AI HANDLER (Fallback)
    # =========================

    return handle_ai(command)