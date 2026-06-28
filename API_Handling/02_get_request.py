import requests

res = requests.get("https://api.github.com/events")

print(res.status_code, type(res.status_code)) #return int
print(res.headers["content-type"], type(res.headers["content-type"])) #return str
print(res.encoding, type(res.encoding)) #return str
print(res.text, type(res.text)) #return str
print(res.json(), type(res.json())) #can return either a Python dict or a list, depending on the JSON returned by the API.

