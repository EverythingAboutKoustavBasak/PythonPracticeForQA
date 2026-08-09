"""
Pretty Print

JSON Helper

Serialization

-------------------------------
flow - 

Gemini
   ↓
Pydantic
   ↓
TestCaseList object
   ↓
.model_dump()
   ↓
Python dictionary
   ↓
save_json()
   ↓
generated_test_cases.json
-----------------------------------
example o/p

{
    "test_cases": [
        {
            "test_case_id": "TC001",
            "title": "Verify valid login",
            "preconditions": "User has valid credentials",
            "steps": [
                "Open the login page",
                "Enter valid username",
                "Enter valid password",
                "Click Login"
            ],
            "expected_result": "User is successfully logged in",
            "priority": "High",
            "status": "Not Run"
        }
    ]
}

"""

import json
from pathlib import Path
from typing import Any

"""
save_json() does:
Python object
     ↓
JSON file
"""

def save_json(data: Any, file_path: str) -> None:
    """
    Saves data to a JSON file.

    Args:
        data (Any): Data to be saved.
        file_path (str): Destination JSON file path.

    Raises:
        OSError: If the file cannot be created or written.
        TypeError: If the data is not JSON serializable.
    """

    path = Path(file_path)

    # Create parent directory if it does not exist
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False #allows Unicode characters to be written naturally.Without it, some Unicode characters may be escaped.
        )

"""
load_json() does:
JSON file
     ↓
Python object
"""

def load_json(file_path: str) -> Any:
    """
    Loads data from a JSON file.

    Args:
        file_path (str): Path of the JSON file.

    Returns:
        Any: Parsed JSON data.

    Raises:
        FileNotFoundError: If the JSON file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """

    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
