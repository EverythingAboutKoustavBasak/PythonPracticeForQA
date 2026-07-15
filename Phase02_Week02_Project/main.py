from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import sys
from pydantic import BaseModel
from typing import Literal
import httpx
from google.genai import errors



print("=================================================")
print("       AI-POWERED TEST CASE GENERATOR       ")
print("=================================================")

#create custome exceptions

class MissingAPIKeyOrModel(Exception):
    # Raised when the Gemini API key or model name is missing.
    pass

class EmptyUserStory(Exception):
    #Raised when the file(user story) is empty or missing
    pass
 
class InvalidAIResponse(Exception):
    #Raised when the ai responses is not formated or empty
    pass   




# Load environment variables
load_dotenv()

# Step: 1 (	Load API key safely	from .env file)
print("[STEP 1] Loading API key and API model from .env - Starting...")
#Reading the values from .env file
api_key = os.getenv("GEMINI_API_KEY", "").strip() #missing environment variables default to "", and .strip() removes accidental spaces.
model_name = os.getenv("GEMINI_API_MODEL", "").strip() #missing environment variables default to "", and .strip() removes accidental spaces.

try:
    if not api_key:
        raise MissingAPIKeyOrModel(
            "GEMINI_API_KEY is missing or empty."
        )

    if not model_name:
        raise MissingAPIKeyOrModel(
            "GEMINI_API_MODEL is missing or empty."
        )

except MissingAPIKeyOrModel as e:
    print(f"Configuration Error: {e}")
    sys.exit(1) # sys.exit(0) → Successful termination , sys.exit(1) → Terminated because of an error

print("[STEP 1] Loading API key and API model from .env... Done✅")

#step: 2 (Read user story from a .txt file)
print("[STEP 2] Reading user story from user_story.txt - Starting...")

user_story_txt_file_pah = "user_story.txt"
try:
    # Check whether the file exists
    if not os.path.exists(user_story_txt_file_pah):
        raise EmptyUserStory("user_story.txt is missing.")

    # Read the file
    with open("user_story.txt", "r", encoding="utf-8") as file:
        user_story_data = file.read().strip()  # And strip() handles whitespace-only files - removes extra whitespace from the beginning and end. also helps detect whitespace-only files:

    # Check whether the file is empty
    if not user_story_data:
        raise EmptyUserStory("user_story.txt is empty.")

except EmptyUserStory as e:
    print(f"Error: {e}")
    sys.exit(1)
    
print("[STEP 2] Reading user story from user_story.txt... Done✅")
# print(user_story_data)


# Step: 3 (	Build the prompt)
print("[STEP 3] Building prompt - Starting...")

# create system prompts
SYSTEM_PROMPT = """
You are a Senior QA Engineer.

Analyze the provided user story and acceptance criteria.

Generate comprehensive test cases covering:
- Functional scenarios
- Positive scenarios
- Negative scenarios
- Boundary scenarios
- Edge cases

Ensure test cases are clear, non-duplicative, and directly traceable
to the requirements.

The test cases must only cover behavior explicitly stated or logically required by the user story and acceptance criteria.
Do not assume unsupported functionality.
"""




"""
Pydantic Approach - validate the response data against TestCase Model
TestCase is a Pydantic model that can define, validate, and structure data.
This code creates a data model/schema using Pydantic. It defines exactly what one test case should look like.
"""
class TestCase(BaseModel):
    test_case_id: str
    title: str
    preconditions: str
    steps: list[str]
    expected_result: str
    priority: Literal[
        "High",
        "Medium",
        "Low"
    ]
    test_type: Literal[
        "Functional",
        "Positive",
        "Negative",
        "Boundary",
        "Edge Case"
    ]
    Status: Literal["Run", "Not Run"]

#user story with acceptance criteria         
user_prompt = user_story_data

print("[STEP 3] Building prompt... Done✅")


#Step: 4 (Call Gemini API with controlled parameters)
print("[STEP 4] Calling Gemini API with configaration - Starting...")


#setup client 
client = genai.Client(api_key=api_key)

#calling api and get the responses
try:
    
    response = client.models.generate_content(
        
        model=model_name,
        contents= user_prompt,
        
        #configaration setup
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature = 0.1,
            max_output_tokens = 3000,
            response_mime_type="application/json", #to force an AI model to output its response strictly as a raw, valid JSON object
            response_schema=list[TestCase] #Return a list of test cases, and every test case should follow the TestCase structure.
        )
    )
    

# Network-related failures - 
except (httpx.TimeoutException, httpx.ConnectError) as e:
    print(f"Network Error: Unable to connect to the Gemini API. {e}")
    sys.exit(1)

# Gemini API-related failures
except errors.APIError as e:
    print(f"Gemini API Error: {e}")
    sys.exit(1)

# Any unexpected Python/program error
except Exception as e:
    print(f"Unexpected Error: {e}")
    sys.exit(1)

print("[STEP 4] Calling Gemini API with configaration... Done✅")
# print(response.parsed) #get the test cases in a list type

"""
#step: 5 (Parsing AI Response - no need 1st, 2nd and 3rd point to implement 
beacuse of response.parsed all ready provide the list of data becuase i used the response_schema=list[TestCase]
and used the pydantic model approach

"""
print("[STEP 5] Parsing AI Response - Starting...")

try:
    test_cases = response.parsed    # test_cases = response.parsed #already parsed using your Pydantic schema - response_schema=list[TestCase] , Return List

    if not test_cases: #Checking if not test_cases: catches both None and an empty list.
        raise InvalidAIResponse(
            "Gemini returned an empty or invalid response."
        )

except InvalidAIResponse as e:
    print(f"Gemini Response Error: {e}")
    sys.exit(1)

print("[STEP 5] Parsing AI Response... Done ✅")

#step: 6 (Print formatted terminal report)
print("[STEP 6] Print formatted terminal report - Starting")


print("========================================")
print("      GENERATED TEST CASES REPORT")
print("========================================")

for index, tc in enumerate(test_cases, start=1):

    print(f"\nTest Case {index} : {tc.test_case_id}")
    print(f"Title        : {tc.title}")
    print(f"Priority     : {tc.priority}")
    print(f"Test Type    : {tc.test_type}")
    print(f"Precondition : {tc.preconditions}")

    print("Steps:")
    for step_no, step in enumerate(tc.steps, start=1):
        print(f"   {step_no}. {step}")

    print(f"Expected     : {tc.expected_result}")
    print(f"Status       : {tc.Status}")

    print("-" * 40)

#test priority count 
high_count = 0
medium_count = 0
low_count = 0

for tc in test_cases:

    if tc.priority == "High":
        high_count += 1

    elif tc.priority == "Medium":
        medium_count += 1

    elif tc.priority == "Low":
        low_count += 1


#print the count 
print("=" * 40)

print(
    f"Total Generated : {len(test_cases)} | "
    f"High : {high_count} | "
    f"Medium : {medium_count} | "
    f"Low : {low_count}"
)

print("=" * 40)

print("[STEP 6] Print formatted terminal report... Done ✅")


#step: 7 (Save to .json file)
print("[STEP 7] Save to JSON File - Starting...")
"""
Why do we use model_dump() before json.dump()?
answer:
response.parsed returns Pydantic model objects (TestCase), not plain Python dictionaries. 
The json.dump() function can only serialize standard Python data types like dictionaries, lists, strings, and numbers. 
Therefore, we first call model_dump() on each Pydantic object to convert it into a dictionary, 
and then json.dump() can successfully write it as JSON.

Why did you use json.dump() instead of file.write()?
answer: 
file.write() can only write strings. My data was a Python list of dictionaries, not a string. 
The json.dump() function automatically serializes Python objects into valid JSON and writes them to the file. 
If I already had a JSON string, such as response.text, then I could use file.write() directly.

point to be noted to write a file
Use json.dump() when you have a Python object (list, dict, etc.).
Use file.write() when you already have a string.

"""
import json

try:
    # Convert Pydantic objects into dictionaries
    json_test_case = []  #it contain a test cases in a list of dictionaries way
    for each_test_case_item in test_cases:
        json_test_case.append(each_test_case_item.model_dump()) 

    # Save the dictionaries into a JSON file
    with open("generated_test_cases.json", "w", encoding="utf-8") as file:
        json.dump(json_test_case, file, indent=4)
        
        
except Exception as e:
    print(f"Error while saving JSON file: {e}")
    sys.exit(1)

print("[STEP 7] Save to JSON File... Done ✅")



"""
The assignment asked for json.loads(). Why did you use response.parsed instead?
Ans -
The assignment's objective was to obtain structured JSON from Gemini. 
I chose response_schema with Pydantic because it validates the AI response against a predefined schema, 
removes the need for manual json.loads(), and prevents malformed outputs from propagating through the application.
In production, I would prefer schema validation over manual parsing because it's safer and more maintainable. 
If the goal is specifically to demonstrate json.loads(), I can also implement that approach.


"""
