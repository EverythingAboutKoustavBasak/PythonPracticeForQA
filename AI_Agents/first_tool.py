import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


# =========================================================
# 1. Load environment variables
# =========================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_API_MODEL", "gemini-3.5-flash")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set")


# =========================================================
# 2. Create Gemini client
# =========================================================

client = genai.Client(api_key=API_KEY)


# =========================================================
# 3. python funtion to create a test case
# =========================================================

def create_test_case(
    title: str,
    steps: list[str],
    expected: str
) -> dict:
    """
    Create a software test case.

    Args:
        title: The title of the test case.
        steps: List of steps required to execute the test.
        expected: Expected result after executing the test.

    Returns:
        A dictionary containing the created test case.
    """

    test_case = {
        "title": title,
        "steps": steps,
        "expected": expected
    }

    print("\n========== TOOL CALLED ==========")
    print("create_test_case()")
    print("=================================\n")

    return test_case


# =========================================================
# 4. Ask Gemini to use the tool
# =========================================================

prompt = """
Create one positive test case for this user story:

User should be able to login using a valid email address
and valid password.
"""


response = client.models.generate_content(
    model=MODEL,
    contents=prompt,
    
    config=types.GenerateContentConfig(
        temperature = 0.1,
        max_output_tokens = 2000,
        tools=[create_test_case] #the command that makes the function available to the model or makes the function to a tool
        
    )
)


# =========================================================
# 5. Print final response
# =========================================================

print("\n========== GEMINI RESPONSE ==========")
print(response.text)
print("=====================================")