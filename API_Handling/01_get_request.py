import requests

res = requests.get("https://www.google.com")

data = res.text
print("---------------------------------------------")
print(type(data)) #it is a string data
print("---------------------------------------------")
print(data)
with open("index.html", "w") as f:
    f.write(res.text)