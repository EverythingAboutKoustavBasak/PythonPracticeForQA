from dotenv import load_dotenv
import os
from google import genai
import json

# Load environment variables
load_dotenv()

# Read values from .env
api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_API_MODEL")

# # Create Gemini client. - A client is an object that knows how to communicate with a server.
# #Think of it as a messenger between your Python program and Google's Gemini servers.
client = genai.Client(api_key=api_key)


# models = client.models.list()
# for model in models:
#     print(model.name)

# Prompts
prompt1 = "What is Python?"
prompt2 = "What is software testing?"
prompt3 = "What is shift left testing?"

try:
    # Generate response
    response = client.models.generate_content(
        model=model_name,
        contents=prompt3
    )

    #print in a consol
    print(response.text)


    # Create my own JSON object to save the respons 
    response_data = {
        "prompt": prompt3,
        "model": model_name,
        "response": response.text
    }

    # Save JSON to a file
    with open("gemini_response.json", "w", encoding="utf-8") as file:
        json.dump(response_data, file, indent=4)

    print("\nResponse saved successfully!")
    
    
except Exception as e:
    print("\nError occurred:")
    print(e)
