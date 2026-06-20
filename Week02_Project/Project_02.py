test_case_list=[]
test_case_passed_count = 0
test_case_failed_count = 0
test_case_skipped_count = 0



#custom exception
class EnterWrongInput(Exception):
    pass    

#function which is evaluated the test case is passed or failled
def create_test_case(title, steps, expected, actual):
    
    if(expected==actual):
        status = "passed"
    else:
        status = "failed"
    
    return {
        "title" : title, 
        "steps" : steps ,
        "expected" : expected, 
        "actual" : actual,
        "status" : status
    }

print("=============================================")
print("       TEST CASE CREATOR & RUNNER            ")
print("=============================================")


try: 
    #number of test cases   
    user_input_number_of_test_cases = int(input("How many number of Test Cases you want to enter = "))
    if(user_input_number_of_test_cases<=0 ):
        raise EnterWrongInput("Please enter a number greater than 0")

except ValueError:
    print("Please enter only numbers")
    exit()
except EnterWrongInput as e:
    print(e)
    exit()
    

#collect inputs → call function → append to list    
for test_case in range(1, user_input_number_of_test_cases+1):
    print(f"------- Test Case #{test_case} -------")
    test_case_titel = input(f"Enter Test Case#{test_case} Titel: ")
    test_case_steps = input(f"Enter Test Case#{test_case} Steps (Steps Should be separated by comma(,)):  ").split(",")
    test_case_expected_value = input(f"Enter Test Case#{test_case} Expected Value: ").lower()
    test_case_actual_value = input(f"Enter Test Case#{test_case} Actual Value: ").lower()
    
    test_case_create = create_test_case(test_case_titel, test_case_steps, test_case_expected_value, test_case_actual_value)
    
    # passed/fail Count of TC
    if test_case_create["status"] == "passed":
        test_case_passed_count += 1
    elif test_case_create["status"] == "failed":
        test_case_failed_count += 1
        
    #add the test cases to the lists
    test_case_list.append(test_case_create)
   

# print(create_test_case(test_case_titel, test_case_steps, test_case_expected_value, test_case_actual_value))
# print(f"Test Case List = {test_case_list}")

print("=============================================")
print("            TEST RUN SUMMARY                 ")
print("=============================================")


#Printing The OUTPUT RESULT
for index, item in enumerate(test_case_list, start=1):   #  enumerate works naturally for numbering the test cases
    print(f"Test Case# {index}       : {item['title']}")
    print(f"Test Steps         : {item['steps']}")
    print(f"Test Expectation   : {item['expected']}")
    print(f"Test Actual Result : {item['actual']}")
    print(f"Test Case Status   : {item['status']}")
    if(item['status']=="passed"):
        print(f"Test Result        : Test completed successfully.")
        # test_case_passed_count+=1
    elif(item['status']=="failed"):
        print(f"Test Result        : Defect needs to be raised!")
        # test_case_failed_count+=1
    print("----------------------------------------------------------")

print("=============================================================")    
print(f"Total: {len(test_case_list)} | Pass: {test_case_passed_count} | Fail: {test_case_failed_count} | Skipped: {test_case_skipped_count}")
print("=============================================================")