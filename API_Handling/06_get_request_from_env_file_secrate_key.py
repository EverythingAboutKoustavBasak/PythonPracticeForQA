from dotenv import load_dotenv
import os
import requests

load_dotenv() # Load variables from .env

token = os.getenv("API_TOKEN")
base_url = os.getenv("BASE_URL")

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    f"{base_url}/headers",
    headers=headers
)

print(response.status_code)
# print("Status Code:", response.status_code)
# print("Content-Type:", response.headers.get("Content-Type"))
# print("Response Text:")
# print(response.text)
print(response.json())