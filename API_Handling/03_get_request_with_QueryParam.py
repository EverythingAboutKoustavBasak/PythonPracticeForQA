import requests

query_param = {"key1":"value1", "key2":"value2"}


res = requests.get("https://httpbin.org/get", params=query_param) 

print("Status Code:", res.status_code)
print("Content-Type:", res.headers.get("Content-Type"))

print(res.json())