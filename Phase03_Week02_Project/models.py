from pydantic import BaseModel
from typing import Literal


class TestCase(BaseModel):
    test_case_id: str
    module_name: str
    title: str
    preconditions: list[str]
    steps: list[str]
    expected_result: str

    priority: Literal[
        "High",
        "Medium",
        "Low"
    ]

    test_type: Literal[
        "Functional",
        "Positive",
        "Negative",
        "Boundary",
        "Edge Case"
    ]

class TestCaseResponse(BaseModel):
    test_cases: list[TestCase]
    
    

#Automation Script structure
class JavaFile(BaseModel):
    file_name: str
    code: str


class AutomationResponse(BaseModel):
    module_name: str
    page_object: JavaFile
    test_class: JavaFile