"""
Contains only Pydantic models.

Pydantic models for the AI Test Case Generator.

These models define the response schema expected from Gemini.
"""

from typing import Literal

from pydantic import BaseModel, Field


class TestCase(BaseModel):
    """
    Represents a single software test case.
    """

    test_case_id: str = Field(
        description="Unique identifier of the test case."
    )

    title: str = Field(
        description="Short title describing the test case."
    )

    preconditions: str = Field(
        description="Conditions that must be satisfied before execution."
    )

    steps: list[str] = Field(
        description="Ordered list of execution steps."
    )

    expected_result: str = Field(
        description="Expected outcome after executing the test."
    )

    priority: Literal[
        "High",
        "Medium",
        "Low"
    ] = Field(
        description="Business priority of the test case."
    )

    status: Literal[
        "Not Run"
    ] = Field(
        description="Execution status of the test case."
    )


class TestCaseList(BaseModel):
    """
    Represents the complete AI response.
    """

    test_cases: list[TestCase]