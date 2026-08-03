"""
Contains project configuration.
Gemini API setting like Madel name, Temparature etc...

"""

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# ==========================================================
# Gemini Configuration
# ==========================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in .env")

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# ==========================================================
# AI Configuration
# ==========================================================

TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))
MAX_OUTPUT_TOKENS = int(os.getenv("MAX_OUTPUT_TOKENS", "1000"))

# ==========================================================
# Retry Configuration
# ==========================================================

MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
RETRY_DELAY = int(os.getenv("RETRY_DELAY", "2"))

# ==========================================================
# API Configuration
# ==========================================================

POST_API_URL = os.getenv(
    "POST_API_URL",
    "https://jsonplaceholder.typicode.com/posts"
)