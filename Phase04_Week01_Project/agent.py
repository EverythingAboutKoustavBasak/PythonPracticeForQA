import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types


# ============================================================
# 1. Load environment variables
# ============================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not configured.")


# ============================================================
# 2. Create Gemini client
# ============================================================

client = genai.Client(api_key=API_KEY)


# ============================================================
# 3. TOOL 1: read_user_story()
# ============================================================
#
# This tool reads the user story from a .txt file.
#
# ============================================================

def read_user_story() -> str:
    """
    Read the user story from user_story.txt.

    Returns:
        The user story text.
    """

    file_path = Path("user_story.txt")

    print("\n========== TOOL: read_user_story ==========")

    if not file_path.exists():
        raise FileNotFoundError(
            f"User story file not found: {file_path}"
        )

    user_story = file_path.read_text(
        encoding="utf-8"
    ).strip()

    if not user_story:
        raise ValueError(
            "user_story.txt is empty."
        )

    print("User story successfully read.")
    print("============================================")

    return user_story


