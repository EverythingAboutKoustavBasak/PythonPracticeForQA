from langchain.tools import tool


import os
from pathlib import Path

from dotenv import load_dotenv

from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


# ============================================================
# 1. Load environment variables
# ============================================================

load_dotenv()


if not os.getenv("GEMINI_API_KEY"):
    raise ValueError(
        "GEMINI_API_KEY is not configured."
    )


# ============================================================
# 2. Create Gemini model through LangChain
# ============================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash"
)




# ============================================================
# 3. TOOL 1: Read User Story
# ============================================================
@tool #The LangChain @tool decorator converts our Python function into a tool that the model can understand and call. Its docstring becomes the tool description used by the model.
def read_user_story() -> str:
    """Read the user story from user_story.txt and return its contents."""

    file_path = Path("user_story.txt")

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

    return user_story



# ============================================================
# 4. TOOL 2: Generate Test Cases
# ============================================================
@tool
def generate_test_cases(user_story: str) -> str:
    """Generate comprehensive SDET test cases from the supplied user story."""

    prompt = f"""
You are an experienced SDET.

Your ONLY task is to generate test cases from the EXACT
user story provided below.

IMPORTANT RULES:

1. Use ONLY the supplied user story.
2. Do NOT invent another user story.
3. Do NOT use examples from previous conversations.
4. Do NOT introduce unrelated features.
5. Every test case must be directly traceable to the user story.
6. Generate positive, negative, boundary, and edge cases
   only when relevant.
7. Do not add test cases unrelated to the user story.

USER STORY
==================================================
{user_story}
==================================================

Return only the test cases.
"""

    response = llm.invoke(prompt)

    return response.text