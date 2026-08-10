"""
Responsible for - Generate/display application reports

Print Test Cases

↓

Priority Summary

↓

Console Formatting

---------------------------------
                    main.py
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
   gemini_service             api_service
          │                         │
          ▼                         ▼
       Gemini                  POST API
          │                         │
          ▼                         ▼
    TestCaseList              API Results
          │                         │
          └────────────┬────────────┘
                       ▼
                report_service
                       │
                       ▼
                  Console Report


"""


# ==========================================================
# Generated Test Cases Report
# ==========================================================

def generate_test_case_report(test_cases) -> None:
    """
    Prints the generated test cases report.

    Args:
        test_cases: TestCaseList Pydantic model.
    """

    print("\n")
    print("=" * 50)
    print("          GENERATED TEST CASES REPORT")
    print("=" * 50)

    for index, test_case in enumerate(
        test_cases.test_cases,
        start=1
    ):

        print()

        print(
            f"Test Case {index} : {test_case.test_case_id}"
        )

        print(
            f"Title       : {test_case.title}"
        )

        print(
            f"Priority    : {test_case.priority}"
        )

        print(
            f"Precondition: {test_case.preconditions}"
        )

        print("Steps       :")

        for step_number, step in enumerate(
            test_case.steps,
            start=1
        ):
            print(
                f"    {step_number}. {step}"
            )

        print(
            f"Expected    : {test_case.expected_result}"
        )

        print(
            f"Status      : {test_case.status}"
        )

        print("-" * 50)

    # ------------------------------------------------------
    # Priority Summary
    # ------------------------------------------------------

    total = len(test_cases.test_cases)

    high_count = 0
    medium_count = 0
    low_count = 0

    for test_case in test_cases.test_cases:

        if test_case.priority == "High":
            high_count += 1

        elif test_case.priority == "Medium":
            medium_count += 1

        elif test_case.priority == "Low":
            low_count += 1

    print()

    print(
        f"Total: {total} | "
        f"High: {high_count} | "
        f"Medium: {medium_count} | "
        f"Low: {low_count}"
    )


# ==========================================================
# API Posting Report
# ==========================================================

def generate_posting_report(
    posting_results: list[dict]
) -> None:
    """
    Prints the API posting report.

    Args:
        posting_results (list[dict]):
            Results returned by the API service.
    """

    print("\n")
    print("=" * 50)
    print("                POSTING REPORT")
    print("=" * 50)

    total = len(posting_results)

    success_count = 0
    failed_count = 0

    for index, result in enumerate(
        posting_results,
        start=1
    ):

        print()

        print(
            f"Test Case {index} : "
            f"{result['title']}"
        )

        print(
            f"    API Status : "
            f"{result['status']}"
        )

        print(
            f"    Status Code: "
            f"{result['status_code']}"
        )

        print(
            f"    Generated ID: "
            f"{result['generated_id']}"
        )

        print("-" * 50)

        # --------------------------------------------------
        # Count Success / Failure
        # --------------------------------------------------

        if result["status"] == "Request Successfully":
            success_count += 1

        else:
            failed_count += 1

    print()

    print("=" * 50)

    print(
        f"Total Posted: {total} | "
        f"Success: {success_count} | "
        f"Failed: {failed_count}"
    )

    print("=" * 50)