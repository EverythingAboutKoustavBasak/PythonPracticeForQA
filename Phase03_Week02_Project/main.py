from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import sys


# Load environment variables
load_dotenv()

# Step: 1 (	Load API key safely	from .env file)
print("[STEP 1] Loading API key and API model from .env - Starting...")
#Reading the values from .env file
api_key = os.getenv("GEMINI_API_KEY", "").strip() #missing environment variables default to "", and .strip() removes accidental spaces.
model_name = os.getenv("GEMINI_API_MODEL", "").strip() #missing environment variables default to "", and .strip() removes accidental spaces.
