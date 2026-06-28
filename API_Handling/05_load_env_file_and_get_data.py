from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

token = os.getenv("API_TOKEN")
base_url = os.getenv("BASE_URL")

print(token)
print(base_url)