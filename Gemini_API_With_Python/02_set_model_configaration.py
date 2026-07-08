'''

| Configuration                                   | Purpose                               | Recommended for SDET | Why it's useful                                 |
| ----------------------------------------------- | ------------------------------------- | -------------------- | ----------------------------------------------- |
| `temperature`                                   | Controls randomness                   | ⭐⭐⭐⭐⭐         | Generate consistent test cases                  |
| `max_output_tokens`                             | Limits response length                | ⭐⭐⭐⭐⭐         | Prevent truncated or overly long responses      |
| `response_mime_type`                            | Specifies output format               | ⭐⭐⭐⭐⭐         | Return JSON instead of plain text               |
| `response_schema`                               | Defines JSON structure                | ⭐⭐⭐⭐⭐         | Structured output for Excel, ADO, databases     |
| `system_instruction`                            | Sets the model's role                 | ⭐⭐⭐⭐⭐         | Make the model behave like a Senior QA Engineer |
| `candidate_count` *(if supported by the model)* | Requests multiple response candidates | ⭐⭐⭐              | Compare alternative test suites                 |
| `top_p`                                         | Controls diversity                    | ⭐⭐⭐              | Fine-tune output diversity                      |
| `top_k`                                         | Limits token selection                | ⭐⭐                | Advanced tuning; rarely needed                  |
| `stop_sequences`                                | Stops generation at specific text     | ⭐⭐⭐              | Prevent unwanted extra output                   |

If I were mentoring an SDET who wants to build AI-powered QA tools, I'd recommend learning them in this order:


'''






from google import genai
from google.genai import types
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_API_MODEL")

SYSTEM_PROMPT = """
                You are a Senior QA Engineer.

                Generate:
                - Functional Test Cases
                - Negative Test Cases
                - Boundary Test Cases
                - Edge Cases

                Return JSON only.

                Include:
                - Test Case ID
                - Title
                - Preconditions
                - Steps
                - Expected Result
                - Priority
                - Test Type
"""
user_prompt1 = """
        wite test cases for login features 
        make sure all functionality should be covered including positive, negative, edge cases
        """
user_prompt2 = """
        wite test cases for the belowuser story 
        story Description - As Liza (client), I want to be able to click anywhere in a row within Call Center Insights (not just a "Details" button), so that I can navigate to the call's Insights tab more quickly.
        Acceptance Criteria - Clicking anywhere within a table row navigates the user to that call's Insights/detail view.
        The existing "Details" button/link continues to function as an alternative entry point.
        Change is applied consistently across all rows in the Call Center Insights table.

        """

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

responses = client.models.generate_content(
    model = model_name,
    contents = user_prompt2,
    
    #configaration setup
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        temperature = 0.1,
        max_output_tokens = 3000

    )
    
)

print(responses.text)
print(type(responses))