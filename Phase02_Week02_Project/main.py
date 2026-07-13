from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import sys


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
print(user_story_data)


