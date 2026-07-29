import os
import sys
import json

from google import genai
from google.genai import types
from dotenv import load_dotenv

from system_prompts import DEFECT_SYSTEM_PROMPT


# Load environment variables
load_dotenv()

#Reading the values from .env file
api_key = os.getenv("GEMINI_API_KEY", "").strip() #missing environment variables default to "", and .strip() removes accidental spaces.
model_name = os.getenv("GEMINI_API_MODEL", "").strip() #missing environment variables default to "", and .strip() removes accidental spaces.

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


#Create Gemini client
client = genai.Client(api_key=api_key)

# Call Gemini
try:
    
    response = client.models.generate_content(
            
            model=model_name,
            contents= f"""
            Analyze the following automated test failure.

            Generate a software defect in the required JSON format.
            
            {failure_log}
            """,
            
            #configaration setup
            config=types.GenerateContentConfig(
                system_instruction=DEFECT_SYSTEM_PROMPT,
                temperature = 0.1,
                max_output_tokens = 2000,
                response_mime_type="application/json", #to force an AI model to output its response strictly as a raw, valid JSON object
            )
        )

except Exception as e:
    print(f"AI Calling Error !!! - {e}")
    sys.exit(1) #program terminated beacuse of error


# Check if response is empty
if not response.text:
    print("No response received from AI.")
    sys.exit(1)

# Convert JSON string to Python dictionary
try:
    defect_data = json.loads(response.text)
except Exception as e:
    print(f"Invalid JSON returned by AI: {e}")
    sys.exit(1)
    
# Save to JSON file
try:
    with open("defect.json", "w", encoding="utf-8") as file:
        json.dump(defect_data, file, indent=4) #dump, converts the Python dictionary into JSON and writes it directly to the file

    print("Defect saved successfully to defect.json - ✅")

except Exception as e:
    print(f"Error saving JSON file: {e}")
    
    
"""

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
