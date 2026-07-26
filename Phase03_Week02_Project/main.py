import os
import sys
import json


from google import genai
from google.genai import types
from dotenv import load_dotenv
from pathlib import Path

from models import TestCaseResponse
from prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

#Reading the values from .env file
api_key = os.getenv("GEMINI_API_KEY", "").strip() #missing environment variables default to "", and .strip() removes accidental spaces.
model_name = os.getenv("GEMINI_API_MODEL", "").strip() #missing environment variables default to "", and .strip() removes accidental spaces.



#------------------------------------------------
#stage 1 - tc genarate 
#------------------------------------------------

#Create Gemini client
client = genai.Client(api_key=api_key)

#user story
user_story = """
As a registered user,
I want to login using my username and password
so that I can access my account.

Acceptance Criteria:

1. User should be able to enter username.
2. User should be able to enter password.
3. User should be able to click the Login button.
4. Valid credentials should redirect the user to Dashboard.
5. Invalid credentials should display an error message.
6. Username and password are mandatory.
"""

# Call Gemini
try:
    
    response = client.models.generate_content(
            
            model=model_name,
            contents= f"""
            Generate test cases for the following user story:
            
            {user_story}
            """,
            
            #configaration setup
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature = 0.1,
                max_output_tokens = 5000,
                response_mime_type="application/json", #to force an AI model to output its response strictly as a raw, valid JSON object
                response_schema=TestCaseResponse #Return a list of test cases, and every test case should follow the TestCase structure.
            )
        )

except Exception:
    print("AI Calling Error !!!")
    sys.exit(1) #program terminated beacuse of error


test_case_response = response.parsed

#create output folder
output_folder = Path("output/test-case")
output_folder.mkdir(
    parents=True,
    exist_ok=True
)

#Create test case JSON file
output_file = output_folder / "test_cases.json"


with open(output_file, "w", encoding="utf-8") as file:

    json.dump(
        test_case_response.model_dump(),
        file,
        indent=4
    )

print("Test cases generated successfully!")
print(f"File created: {output_file}")

#End of Stage-1 (Genarating test case)