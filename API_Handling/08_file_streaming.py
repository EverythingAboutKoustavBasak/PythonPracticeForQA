"""
Without Streaming
-------------------------
Server
   │
   ▼
Entire File
   │
   ▼
RAM (Memory)
   │
   ▼
Hard Disk

Memory usage is high.

With Streaming
----------------------
Server
   │
   ▼
Small Chunk (8 KB)
   │
   ▼
Hard Disk

Next Chunk
   │
   ▼
Hard Disk

Next Chunk
   │
   ▼
Hard Disk

Only a small chunk is kept in memory at a time. Memory usage is very low.



Why Use File Streaming?
--------------------------------
Advantages:
Saves RAM
Faster for large files
Suitable for videos, ZIP files, PDFs, ISO files
Professional approach

Interview Question
--------------------------------
Q. Why do we use stream=True?
---------------------------------
Answer - To download large files efficiently without loading the entire file into memory. 
The file is downloaded in small chunks, reducing RAM usage.

Q. What does iter_content() do?
-----------------------------------
Answer - It reads the HTTP response in small chunks instead of loading the whole response into memory.


| `response.content`    | `response.iter_content()` |
| --------------------- | ------------------------- |
| Downloads entire file | Downloads in chunks       |
| High memory usage     | Low memory usage          |
| Good for small files  | Best for large files      |
| Simpler code          | More efficient            |


"""
import requests

image_url = "https://picsum.photos/600"

response = requests.get(image_url, stream=True)

if response.status_code == 200:
    with open("image2.jpg", "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print("Image Downloaded Successfully")
else:
    print("Download Failed")  