"""
User Prompt Builder

This module builds the user prompt dynamically
by inserting the user story into the prompt template.

Q: Why create a build_prompt() function instead of calling .format() directly?
build_prompt() encapsulates all prompt construction logic in one place. 
Today it inserts the user story into a template, but in the future it can also validate input, clean whitespace, 
add metadata, or preprocess the text. This follows the Single Responsibility Principle (SRP) by keeping main.py 
focused on orchestration while build_prompt() is responsible only for creating the final prompt sent to the AI.

main.py
    │
    ▼
Read user_story.txt
    │
    ▼
build_prompt(user_story)
    │
    ▼
Final User Prompt
    │
    ▼
Gemini
          +
SYSTEM_PROMPT
"""

USER_PROMPT_TEMPLATE = """
Generate software test cases for the following user story.

User Story:
{user_story}

Requirements:

1. Carefully analyze the user story before generating test cases.

2. Generate exactly 5 unique test cases.

3. Ensure the test cases collectively cover:
   - Positive scenarios
   - Negative scenarios
   - Boundary conditions (if applicable)
   - Input validation
   - Business rule validation
   - Error handling (if applicable)

4. Each test case should be:
   - Business-focused
   - Clear
   - Executable
   - Non-duplicated

5. Use only the information available in the user story.

6. Do not assume functionality that is not mentioned.

Generate the response according to the provided response schema.
"""


def build_user_prompt(user_story: str) -> str:
    """
    Builds the final user prompt by inserting the user story
    into the prompt template.

    Args:
        user_story (str): User story read from the input file.

    Returns:
        str: Complete prompt sent to the AI model.
    """
    return USER_PROMPT_TEMPLATE.format(
        user_story=user_story.strip()
    )