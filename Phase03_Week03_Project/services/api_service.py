"""
This is for your external POST API.
The responsibility would be:
------------------------------
Pydantic model
      ↓
api_service.py
      ↓
POST API

It should contain:
------------------------
API URL handling
HTTP POST request
Headers
Request body
Response status handling
API-specific exceptions

It should not contain Gemini logic.



"""


import requests

from config import POST_API_URL

from exceptions import APICallFailed

from models import TestCaseList


def post_test_cases(test_cases: TestCaseList) -> list[dict]:
    """
    Posts generated test cases to the configured API.

    Args:
        test_cases (TestCaseList): Generated test cases represented
            by a Pydantic model.

    Returns:
        list[dict]: Results returned for each test case.

    Raises:
        APICallFailed: If the API request fails.
    """

    posting_results = []

    for test_case in test_cases.test_cases:

        try:
            response = requests.post(
                POST_API_URL,
                json=test_case.model_dump(),
                timeout=30,
            )

            response.raise_for_status()

            response_data = response.json()

            posting_results.append(
                {
                    "test_case_id": test_case.test_case_id,
                    "title": test_case.title,
                    "status": "Request Successfully",
                    "status_code": response.status_code,
                    "generated_id": response_data.get("id"),
                }
            )

        except requests.RequestException as exc:

            if exc.response is not None:
                status_code = exc.response.status_code
            else:
                status_code = None

            posting_results.append(
                {
                    "test_case_id": test_case.test_case_id,
                    "title": test_case.title,
                    "status": "Request Failed",
                     "status_code": status_code,
                    "generated_id": None,
                }
            )

    return posting_results

