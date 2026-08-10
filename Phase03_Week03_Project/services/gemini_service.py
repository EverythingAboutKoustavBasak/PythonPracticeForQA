"""
Responsible for
---------------------
This is responsible for communicating with Gemini.

main.py
   │
   ▼
gemini_service.py
   │
   ▼
Gemini API

It should handle things like:
------------------------------------
Create Gemini client
Send system prompt
Send user prompt
Configure model
Configure temperature
Configure Pydantic response schema
Retry API calls
Return the parsed Pydantic response

"""

import time

from google import genai
from google.genai import types

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    TEMPERATURE,
    MAX_OUTPUT_TOKENS,
    MAX_RETRIES,
    RETRY_DELAY,
)

from exceptions import (
    APICallFailed,
    InvalidAIResponse,
)

from models import TestCaseList

from prompts import SYSTEM_PROMPT


# ==========================================================
# Gemini Client
# ==========================================================

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ==========================================================
# Generate Test Cases
# ==========================================================

def generate_test_cases(user_prompt: str) -> TestCaseList:
    """
    Generates test cases using Gemini.

    Args:
        user_prompt (str): User prompt containing the user story.

    Returns:
        TestCaseList: Gemini response parsed into a Pydantic model.

    Raises:
        APICallFailed: If Gemini fails after all retry attempts.
        InvalidAIResponse: If Gemini returns an invalid response.
    """

    last_exception = None

    for attempt in range(1, MAX_RETRIES + 1):

        try:

            print(
                f"\nAttempt {attempt}/{MAX_RETRIES}"
            )

            # --------------------------------------------------
            # Call Gemini
            # --------------------------------------------------

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=TEMPERATURE,
                    max_output_tokens=MAX_OUTPUT_TOKENS,
                    response_mime_type="application/json",
                    response_schema=TestCaseList,
                ),
            )

            # --------------------------------------------------
            # Get Pydantic parsed response
            # --------------------------------------------------

            parsed_response = response.parsed

            # --------------------------------------------------
            # Validate parsed response
            # --------------------------------------------------

            if parsed_response is None:

                raise InvalidAIResponse(
                    "Gemini returned no parsed response."
                )

            if not isinstance(
                parsed_response,
                TestCaseList
            ):

                raise InvalidAIResponse(
                    "Gemini response is not a valid TestCaseList."
                )

            # --------------------------------------------------
            # Success
            # --------------------------------------------------

            print(
                "Response validated successfully. ✅"
            )

            return parsed_response

        except InvalidAIResponse as exc:

            last_exception = exc

            print(
                f"Attempt {attempt} failed: {exc}"
            )

        except Exception as exc:

            last_exception = exc

            print(
                f"Attempt {attempt} failed: {exc}"
            )

        # ------------------------------------------------------
        # Retry
        # ------------------------------------------------------

        if attempt < MAX_RETRIES:

            print(
                f"Retrying in {RETRY_DELAY} seconds..."
            )

            time.sleep(RETRY_DELAY)

    # ----------------------------------------------------------
    # All attempts failed
    # ----------------------------------------------------------

    raise APICallFailed(
        f"Gemini API failed after "
        f"{MAX_RETRIES} attempts."
    ) from last_exception