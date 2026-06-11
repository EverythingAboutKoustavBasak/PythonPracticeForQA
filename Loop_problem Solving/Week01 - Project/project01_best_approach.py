#List of Dicts Approach
#Consider list of dicts only when duplicate test case names are possible

user_input_for_number_of_test_cases = int(input("How many test cases do you want to enter? = "))
test_case_list = []          #  list instead of dict
count_pass_tc = 0
count_fail_tc = 0
count_skipped_tc = 0

for testcase in range(user_input_for_number_of_test_cases):
    test_case_name = input(f"Test case name #{testcase+1} - ")
    test_case_status = input(f"Test Case #{testcase+1} status (Passed, Failed, Skipped) - ").lower()
    
    #  Each test case is a dict, appended into the list
    test_case_list.append({
        "name": test_case_name,
        "status": test_case_status
    })

print("=====================================")
print("        TEST RUN SUMMARY             ")
print("=====================================")

for index, item in enumerate(test_case_list, start=1):   #  enumerate works naturally for numbering the test cases
    if item["status"] == "passed":
        count_pass_tc += 1
        print(f"Test Case {index}     : {item['name']}")
        print(f"Status          : {item['status']}")
        print("Result          : Test completed successfully.")
        print("---------------------------------------------------")

    elif item["status"] == "failed":
        count_fail_tc += 1
        print(f"Test Case {index}     : {item['name']}")
        print(f"Status          : {item['status']}")
        print("Result          : Defect needs to be raised!")
        print("---------------------------------------------------")

    elif item["status"] == "skipped":
        count_skipped_tc += 1
        print(f"Test Case {index}     : {item['name']}")
        print(f"Status          : {item['status']}")
        print("Result          : Test was skipped. Needs re-run.")
        print("---------------------------------------------------")

    else:
        print(f"Test Case {index}     : {item['name']}")
        print(f"Status          : {item['status']}")
        print("Result          : Unknown status entered.")
        print("---------------------------------------------------")

print("=====================================================")
print(f"Total: {len(test_case_list)} | Pass: {count_pass_tc} | Fail: {count_fail_tc} | Skipped: {count_skipped_tc}")
print("=====================================================")