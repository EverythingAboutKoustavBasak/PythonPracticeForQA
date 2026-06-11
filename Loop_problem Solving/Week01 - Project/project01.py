user_input_for_number_of_test_cases = int(input("How many test cases do you want to enter? = "))
test_case_dict={}
count_pass_tc = 0
count_fail_tc = 0
count_skipped_tc = 0
test_case_number = 0 #this is only for number printing 

for testcase in range(user_input_for_number_of_test_cases):
    
    test_case_name = input(f"Test case name #{testcase+1} - ")
    test_case_status = input(f"Test Case #{testcase+1} status (Pass, Fail, Skipped) - ").lower()
    
    test_case_dict[test_case_name] = test_case_status
    
# print("All the test Cases which you Entered - ", test_case_dict)

print("=====================================")
print("        TEST RUN SUMMARY             ")     
print("=====================================")

for iteam in test_case_dict:
    if(test_case_dict[iteam]=="pass"):
        count_pass_tc = count_pass_tc+1
        test_case_number=test_case_number+1
        print(f"Test Case{test_case_number} Name  : {iteam}")
        print("Test Case Status : ", test_case_dict[iteam])
        print("Result           : Test completed successfully.")
        print("---------------------------------------------------")

    elif(test_case_dict[iteam]=="fail"):
        count_fail_tc = count_fail_tc+1
        test_case_number=test_case_number+1
        print(f"Test Case{test_case_number} Name  : {iteam}")
        print("Test Case Status : ", test_case_dict[iteam])
        print("Result           : Defect needs to be raised!")
        print("---------------------------------------------------")
        
    elif(test_case_dict[iteam]=="skipped"):
        count_skipped_tc = count_skipped_tc+1
        test_case_number=test_case_number+1
        print(f"Test Case{test_case_number} Name  : {iteam}")
        print("Test Case Status : ", test_case_dict[iteam])
        print("Result           : Test was skipped. Needs re-run.")
        print("---------------------------------------------------")
    
    else:
        test_case_number=test_case_number+1
        print(f"Test Case{test_case_number} Name  : {iteam}")
        print(f"Test Case Status : {test_case_dict[iteam]}")
        print("Result           : Unknown status entered.")
        print("---------------------------------------------------")
        
print("=====================================================")
print(f"Total: {len(test_case_dict)} | Pass: {count_pass_tc} | Fail: {count_fail_tc} | Skipped: {count_skipped_tc}")
print("=====================================================")
        
    
    
    
    
