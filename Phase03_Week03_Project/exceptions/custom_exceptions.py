"""
Custom created exception like - 

MissingAPIKey

EmptyUserStory

InvalidAIResponse

APICallFailed

"""
"""
Custom exceptions for the AI Test Case Generator.
"""

class MissingAPIKey(Exception):
    """Raised when the Gemini API key is missing."""

    def __init__(self, message="GEMINI_API_KEY is missing in .env"):
        super().__init__(message)


class EmptyUserStory(Exception):
    """Raised when the user story file is missing or empty."""

    def __init__(self, message="User story is missing or empty."):
        super().__init__(message)


class InvalidAIResponse(Exception):
    """Raised when the AI response fails validation."""

    def __init__(self, message="Invalid AI response."):
        super().__init__(message)


class APICallFailed(Exception):
    """Raised when the Gemini API fails after all retries."""

    def __init__(self, message="Gemini API call failed after retries."):
        super().__init__(message)
        
