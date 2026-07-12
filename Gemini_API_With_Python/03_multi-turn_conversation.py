from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_API_MODEL")

# System prompt
SYSTEM_PROMPT = """
You are a Senior QA Engineer.

Your responsibility is to analyze user stories and acceptance criteria
and generate comprehensive test cases.

Cover:
- Functional Test Cases
- Positive Test Cases
- Negative Test Cases
- Boundary Test Cases
- Edge Cases

Each test case should include:
- Test Case ID
- Title
- Preconditions
- Steps
- Expected Result
- Priority
- Test Type

When the user asks for modifications, use the previously generated
test cases and conversation context.
"""

# Create Gemini client
client = genai.Client(api_key=api_key)

# Create one chat session
chat = client.chats.create(
    model=model_name,
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        temperature=0.1,
        max_output_tokens=3000
    )
)

print("QA Assistant Started")
print("Type 'exit' to stop.\n")

# Multi-turn conversation
while True:

    user_prompt = input("You(User): ")

    if user_prompt.lower().strip() == "exit":
        print("QA Assistant stopped.")
        break
        
    try:
        response = chat.send_message(user_prompt)

        print("\nQA Assistant:")
        print(response.text)
        print()

    except Exception as e:
        print(f"Error: {e}")