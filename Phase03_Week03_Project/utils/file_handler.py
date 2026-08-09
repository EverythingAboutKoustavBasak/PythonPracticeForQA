"""
Read txt

Create folder

---------------------------
main.py
   │
   │ read_file()
   ▼
file_handler.py
   │
   ├── File exists?
   │
   ├── Is it actually a file?
   │
   ├── Read content
   │
   ├── Is content empty?
   │
   ▼
return user_story

-------------------------------

What's the difference between open() and Path.read_text()?
open() is Python's lower-level built-in file API that gives me a file object, 
allowing operations such as reading line by line, writing, seeking, and so on. 
Path.read_text() is a higher-level pathlib convenience method for reading the complete contents 
of a text file while handling the open and close operations internally. For simple text-file reading, 
I prefer Path.read_text() because it is concise; for more control over file processing, 
I use open() with a context manager."
"""

from pathlib import Path

from exceptions import EmptyUserStory


def read_file(file_path: str) -> str:
    """
    Reads and returns the content of a text file.

    Args:
        file_path (str): Path of the file to read.

    Returns:
        str: Content of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        EmptyUserStory: If the file is empty.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    content = path.read_text(encoding="utf-8").strip()

    if not content:
        raise EmptyUserStory()

    return content
