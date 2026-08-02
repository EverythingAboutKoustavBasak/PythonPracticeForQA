import os
import sys
import json
import time


from google import genai
from google.genai import types
from pydantic import ValidationError
from dotenv import load_dotenv

from prompts.defects_prompts.system_prompt import DEFECT_SYSTEM_PROMPT
from prompts.defects_prompts.user_prompt import DEFECT_USER_PROMPT
from models.defect_model import DefectResponse


# Load environment variables
load_dotenv()

#Reading the values from .env file
api_key = os.getenv("GEMINI_API_KEY", "").strip() #missing environment variables default to "", and .strip() removes accidental spaces.
model_name = os.getenv("GEMINI_API_MODEL", "").strip() #missing environment variables default to "", and .strip() removes accidental spaces.

if not api_key:
    print("GEMINI_API_KEY not found.")
    sys.exit(1)

if not model_name:
    print("GEMINI_API_MODEL not found.")
    sys.exit(1)

# -------------------------------
# Sample Failure Log
# -------------------------------
failure_log = """
Test: test_login_valid_credentials

Expected:
User redirected to /dashboard

Actual:
Page remained on /login

Error:
Invalid session token

Exception:
TimeoutException

Stack Trace:
LoginPage.java:42
LoginTest.java:18
"""

# Prepare Prompt using prompt template
user_prompt = DEFECT_USER_PROMPT.format(failure_log=failure_log)



#Create Gemini client
client = genai.Client(api_key=api_key)

#implementing smart retry mechanism
MAX_RETRIES = 3
current_prompt = user_prompt

for attempt in range(1, MAX_RETRIES+1):
    
    # Call Gemini
    try:
        print(f"\nAttempt {attempt}/{MAX_RETRIES}")
        
        response = client.models.generate_content(
                
                model=model_name,
                contents = current_prompt,
                #configaration setup
                config=types.GenerateContentConfig(
                    system_instruction=DEFECT_SYSTEM_PROMPT,
                    temperature = 0.1,
                    max_output_tokens = 2000,
                    response_mime_type="application/json", #to force an AI model to output its response strictly as a raw, valid JSON object
                    response_schema=DefectResponse
                )
            )
        
        # Automatically Parsed & Validated
        validated_response = response.parsed
        
        if validated_response is None:
            raise ValueError("Gemini returned an empty parsed response.")
        
        print("Response validated successfully. ✅ ")
        
        break
        
    except ValidationError as e:

        print(f"Schema Validation Failed ❌")

        if attempt == MAX_RETRIES:
            """
            RuntimeError:
            AI response validation failed after 3 retries.

            Caused by:

            ValidationError
            ...
            
            from e preserves the original ValidationError for debugging.
                        
            """
            
            raise RuntimeError(
                f"AI response validation failed after {MAX_RETRIES} attempts."
            ) from e

        # Smart Retry Prompt
        current_prompt = f"""
            {user_prompt}

            ------------------------------------------------

            Your previous response failed schema validation.

            Validation Errors:

            {e}

            Please regenerate the response.

            Return ONLY valid JSON that matches the required schema.

            Do not omit any required fields.
            """

        print("Retrying...\n")
        time.sleep(5)
        
    except Exception as e:
        print(f"Gemini Error: {e}")
        sys.exit(1) #program terminated beacuse of error


#-------------------------------------------------------------
# Check if response is empty
# if not response.text:
#     print("No response received from AI.")
#     sys.exit(1)

# # Convert JSON string to Python dictionary
# try:
#     defect_data = json.loads(response.text)
# except Exception as e:
#     print(f"Invalid JSON returned by AI: {e}")
#     sys.exit(1)
#-------------------------------------------------------------

    
# Save to JSON file

os.makedirs("output", exist_ok=True)


try:
    with open("output/defect.json", "w", encoding="utf-8") as file:
        json.dump(validated_response.model_dump(), file, indent=4) #dump, converts the Python dictionary into JSON and writes it directly to the file

    print("Defect saved successfully to defect.json - ✅")

except Exception as e:
    print(f"Error saving JSON file: {e}")
    sys.exit(1)
    
"""

Why did you use mkdir(exist_ok=True) or os.makedirs(..., exist_ok=True)?
Ans
I use it to ensure the output directory exists before writing the file. If the folder doesn't exist, Python creates it. 
If it already exists, exist_ok=True prevents a FileExistsError. 
This makes the code more robust and avoids requiring manual folder creation.

Why do we use json.dump(defect_data, file)? Why can't we write defect_data directly?
Ans
defect_data is a Python dictionary, whereas a file can only store text or bytes. 
We use json.dump() to serialize the Python dictionary into JSON format and write it directly to the file.
If we try to write the dictionary directly using file.write(defect_data), 
Python raises a TypeError because write() expects a string, not a dictionary.

json.dump() is used to serialize a Python object into JSON format and write it to a file because 
files cannot directly store Python dictionaries.

What is serialization?
Ans
Serialization is the process of converting a Python object, such as a dictionary or list,
into a format like JSON that can be stored in a file or transmitted over a network.


Why did you use json.loads(response.text)?
Ans
Because response.text is a JSON string returned by the API. To work with it as a Python dictionary, 
I use json.loads(). This allows me to access fields like defect_data["title"], validate the data, 
modify it if needed, and then save it using json.dump().




"""
