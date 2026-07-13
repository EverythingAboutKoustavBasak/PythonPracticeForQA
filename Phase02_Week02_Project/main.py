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





# Load environment variables
load_dotenv()

# Step: 1
print("[STEP 1] Loading API key and API model from .env... Starting")
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

