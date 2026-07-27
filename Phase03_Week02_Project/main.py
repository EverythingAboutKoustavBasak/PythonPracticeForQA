import os
import sys
import json


from google import genai
from google.genai import types
from dotenv import load_dotenv
from pathlib import Path

from models import TestCaseResponse, AutomationResponse
from prompts import TESTCASE_SYSTEM_PROMPT, AUTOMATION_SYSTEM_PROMPT
from collections import defaultdict



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
                system_instruction=TESTCASE_SYSTEM_PROMPT,
                temperature = 0.1,
                max_output_tokens = 5000,
                response_mime_type="application/json", #to force an AI model to output its response strictly as a raw, valid JSON object
                response_schema=TestCaseResponse #Return a list of test cases, and every test case should follow the TestCase structure.
            )
        )

except Exception as e:
    print(f"AI Calling Error !!! - {e}")
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



# ==========================================================
# STAGE 2 - GENERATE JAVA SELENIUM AUTOMATION
# ==========================================================


# ==========================================================
# GROUP TEST CASES BY MODULE
# ==========================================================

'''
We need defaultdict(list) because you want to group multiple test cases under the same module_name 
without manually creating a list for each new module.

Suppose Stage 1 gives:

TC001 → Login
TC002 → Login
TC003 → Profile
TC004 → Login
TC005 → Profile

You want to transform that into:

{
    "Login": [TC001, TC002, TC004],
    "Profile": [TC003, TC005]
}

'''

grouped_test_cases = defaultdict(list)

for test_case in test_case_response.test_cases:
    grouped_test_cases[test_case.module_name].append(test_case)
    



# ==========================================================
# CREATE AUTOMATION OUTPUT DIRECTORY
# ==========================================================

automation_folder = Path("output") / "automation_script"

automation_folder.mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================================
# 12. GENERATE AUTOMATION FOR EACH MODULE
# ==========================================================

for module_name, test_cases in grouped_test_cases.items():

    print(f"\nGenerating automation for module: {module_name}")


    # ------------------------------------------------------
    # Convert module test cases to JSON
    # ------------------------------------------------------

    module_test_cases = []

    for test_case in test_cases:
        module_test_cases.append(
            test_case.model_dump()
        )

    module_test_cases_json = json.dumps(
        module_test_cases,
        indent=4
    )


    # ------------------------------------------------------
    # Call Gemini
    # ------------------------------------------------------
    try:
        
        automation_response = client.models.generate_content(

            model=model_name,

            contents=f"""
                    Generate Java Selenium automation for the following module.

                    Module Name:
                    {module_name}

                    Test Cases:
                    {module_test_cases_json}
                    """,

            config=types.GenerateContentConfig(
                system_instruction=AUTOMATION_SYSTEM_PROMPT,
                temperature=0.1,
                response_mime_type="application/json",
                response_schema=AutomationResponse
            )
        )
    except Exception as e:
        print(
            f"Automation generation failed for "
            f"{module_name}: {e}"
        )
        sys.exit(1)

    # ------------------------------------------------------
    # Get parsed response
    # ------------------------------------------------------

    automation = automation_response.parsed


    if automation is None:
        raise ValueError(
            f"Failed to generate automation for module: {module_name}"
        )


    # ------------------------------------------------------
    # Create Page Object Java file
    # ------------------------------------------------------

    page_file = (
        automation_folder
        / automation.page_object.file_name
    )

    with open(page_file, "w", encoding="utf-8") as file:
        file.write(automation.page_object.code)


    # ------------------------------------------------------
    # Create Test Java file
    # ------------------------------------------------------

    test_file = (
        automation_folder
        / automation.test_class.file_name
    )

    with open(
        test_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            automation.test_class.code
        )


    print(
        f"Page Object created: {page_file}"
    )

    print(
        f"Test class created: {test_file}"
    )


print("\nAll automation scripts generated successfully!")