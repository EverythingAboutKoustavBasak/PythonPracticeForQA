import requests

url = "https://httpbin.org/post"

header_content = {
    "Content-Type": "application/json"
}

payload = {
    "name": "Koustav",
    "city": "Kolkata",
    "age": 24
}

response = requests.post(
    url=url,
    headers=header_content,
    json=payload
)

print(response.status_code)
print(response.json())