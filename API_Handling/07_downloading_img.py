"""
Important Interview Points
Use requests.get() to download a file.
Check response.status_code == 200 before saving.
Use response.content for binary files (images, PDFs, ZIPs, etc.).
Open the file in binary write mode ("wb").
response.text is for text (HTML, XML, JSON as a string).
response.json() is only for JSON responses.


| Response Attribute | Use For                                  |
| ------------------ | ---------------------------------------- |
| `response.text`    | HTML, XML, plain text                    |
| `response.json()`  | JSON responses                           |
| `response.content` | Images, PDFs, ZIPs, Videos (binary data) |


"""
import requests

img_url = "https://picsum.photos/400"

res = requests.get(img_url)

if res.status_code==200:
    with open("img1.jpg", "wb") as file:
        file.write(res.content)
    print("Image downloaded successfully!")
else:
    print("Failed to download image.")
    