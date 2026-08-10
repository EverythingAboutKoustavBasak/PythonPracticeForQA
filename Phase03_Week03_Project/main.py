"""
Yes. Now that we have the major components defined, main.py should be very small because its job is only to orchestrate the complete workflow.
It should not contain Gemini API code, prompt templates, JSON logic, API POST logic, or report formatting.

                    main.py
                       │
                       ▼
             Read user_story.txt
                       │
                       ▼
                  user_story
                       │
                       ▼
                build_prompt()
                       │
                       ▼
                  user_prompt
                       │
                       ▼
             generate_test_cases()
                       │
                       ▼
                   Gemini
                       │
                       ▼
                response.parsed
                       │
                       ▼
                 TestCaseList
                       │
            ┌──────────┼───────────┐
            │          │           │
            ▼          ▼           ▼
          Report     model_dump   API POST
            │          │           │
            ▼          ▼           ▼
         Console     JSON       API Results
                                  │
                                  ▼
                            Posting Report
                            
                            
                            
Why do we use if __name__ == '__main__': in Python?
__name__ is a special Python variable. When a file is executed directly, Python sets __name__ to __main__. 
When the file is imported as a module, __name__ contains the module name. 
Therefore, if __name__ == '__main__': ensures that the main() function executes only 
when the file is run directly and does not execute automatically when the module is imported."

"""
"""
Main entry point for the AI Test Case Generator.

The main module is responsible only for orchestrating
the complete application workflow.
"""

from utils import read_file, save_json

from prompts import build_user_prompt

from services import (
    generate_test_cases,
    post_test_cases,
    generate_test_case_report,
    generate_posting_report,
)


# ==========================================================
# Configuration
# ==========================================================

USER_STORY_FILE = "input/user_story.txt"
OUTPUT_JSON_FILE = "output/generated_test_cases.json"


# ==========================================================
# Main Application
# ==========================================================

def main() -> None:
    """
    Executes the complete AI test case generation workflow.
    """

    try:

        # --------------------------------------------------
        # STEP 1: Read User Story
        # --------------------------------------------------

        print("\n[STEP 1] Reading user story...")

        user_story = read_file(
            USER_STORY_FILE
        )

        print("User story loaded successfully. ✅")


        # --------------------------------------------------
        # STEP 2: Build User Prompt
        # --------------------------------------------------

        print("\n[STEP 2] Building user prompt...")

        user_prompt = build_user_prompt(
            user_story
        )

        print("User prompt created successfully. ✅")


        # --------------------------------------------------
        # STEP 3: Generate Test Cases
        # --------------------------------------------------

        print(
            "\n[STEP 3] Generating test cases using Gemini..."
        )

        test_cases = generate_test_cases(
            user_prompt
        )

        print(
            "Test cases generated successfully. ✅"
        )


        # --------------------------------------------------
        # STEP 4: Generate Test Case Report
        # --------------------------------------------------

        print(
            "\n[STEP 4] Generating test case report..."
        )

        generate_test_case_report(
            test_cases
        )


        # --------------------------------------------------
        # STEP 5: Save JSON
        # --------------------------------------------------

        print(
            "\n[STEP 5] Preparing JSON output..."
        )

        test_case_data = test_cases.model_dump()

        save_json(
            test_case_data,
            OUTPUT_JSON_FILE
        )

        print(
            f"[STEP 5] Saved to "
            f"{OUTPUT_JSON_FILE} ... Done ✅"
        )


        # --------------------------------------------------
        # STEP 6: Post Test Cases
        # --------------------------------------------------

        print(
            "\n[STEP 6] Posting to JSONPlaceholder API..."
        )

        posting_results = post_test_cases(
            test_cases
        )


        # --------------------------------------------------
        # STEP 7: Generate Posting Report
        # --------------------------------------------------

        generate_posting_report(
            posting_results
        )

        print(
            "\nProcess completed successfully. ✅"
        )


    except Exception as exc:

        print(
            f"\nApplication failed: {exc}"
        )


# ==========================================================
# Application Entry Point
# ==========================================================

if __name__ == "__main__":
    main()


