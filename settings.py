"""
Phase 2 Configuration
Ultra Fast AI Agent (Groq Based)
"""

# ==============================
# GROQ CONFIGURATION
# ==============================
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant"

# ==============================
# PERFORMANCE SETTINGS
# ==============================

MAX_TOKENS = 300
TEMPERATURE = 0.3
TOP_P = 1

# ==============================
# AUDIO SETTINGS
# ==============================

AUDIO_OUTPUT_FOLDER = "phase_one/audio"

# ==============================
# AGENT SETTINGS
# ==============================

EXIT_COMMANDS = ["exit", "quit", "stop", "bye"]