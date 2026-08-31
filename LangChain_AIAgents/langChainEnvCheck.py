import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# Load environment variables
load_dotenv()


# Check API key
if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("GOOGLE_API_KEY is not configured.")


# Create Gemini model through LangChain
llm = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
)


# Send request
response = llm.invoke(
    "Explain what an AI agent is in simple terms."
)


print(response.content)