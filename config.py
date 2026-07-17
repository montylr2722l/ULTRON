"""
Global configuration for ULTRON.

Author : Vishnu
Version : 0.4.1
"""

# ===========================
# APPLICATION
# ===========================

APP_NAME = "ULTRON"
VERSION = "0.4.1"
DEBUG = True

# ===========================
# USER
# ===========================

USER_NAME = "Vishnu"

# ===========================
# AI
# ===========================

AI_MODEL = "llama3.2:3b"

# Future Models
# AI_MODEL = "mistral"
# AI_MODEL = "phi3"
# AI_MODEL = "deepseek-r1"

# ===========================
# VOICE
# ===========================

VOICE_RATE = 175
VOICE_VOLUME = 1.0

# ===========================
# CONVERSATION
# ===========================

CONVERSATION_TIMEOUT = 30

# ===========================
# FILE PATHS
# ===========================

MEMORY_FILE = "data/memory.json"
LOG_FILE = "logs/commands.log"

# ===========================
# FUTURE FEATURES
# ===========================

WEATHER_API_KEY = ""
NEWS_API_KEY = ""
GITHUB_TOKEN = ""

DEFAULT_BROWSER = "chrome"

ENABLE_AI_FALLBACK = True
ENABLE_LOGGING = True
ENABLE_MEMORY = True