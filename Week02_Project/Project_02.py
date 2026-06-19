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




try: 
    #number of test cases   
    user_input_number_of_test_cases = int(input("How many number of Test Cases you want to enter = "))
    if(user_input_number_of_test_cases<=0 ):
        raise EnterWrongInput("Please enter a number greater than 0")

except ValueError:
    print("Please enter only numbers")
except EnterWrongInput as e:
    print(e)
    
for test_case in range(1, user_input_number_of_test_cases+1):
    test_case_titel = input(f"Enter Test Case#{test_case} Titel: ")
    test_case_steps = input(f"Enter Test Case#{test_case} Steps (Steps Should be separated by comma(,)):  ")
    test_case_expected_value = input(f"Enter Test Case#{test_case} Expected Value: ").lower()
    test_case_actual_value = input(f"Enter Test Case#{test_case} Actual Value: ").lower()
    
print(create_test_case(test_case_titel, test_case_steps, test_case_expected_value, test_case_actual_value))
    
