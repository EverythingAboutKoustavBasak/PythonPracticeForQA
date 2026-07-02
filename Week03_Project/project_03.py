test_case_list=[]
test_case_passed_count = 0
test_case_failed_count = 0

#custome exception
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
print("           TEST CASE FILE PIPELINE                ")
print("=============================================")

print("[STEP 1] Collecting test cases...")  
try:    
    user_max_no_of_test_cases = int(input("How many number of Test Cases you want to enter = "))
    if(user_max_no_of_test_cases<=0):
        raise EnterWrongInput("Please Enter Greater Than 0")

except EnterWrongInput as e:
    print(e)
    exit()
except ValueError:
    print("Please enter only numbers")
    exit()
 
#STEP 1 — Collect test cases 
#collect inputs → call function → append to list    
for test_case in range(1, user_max_no_of_test_cases+1):
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
    
# print(test_case_list)


   
# Step 2 — Write test cases to a .json file
import json

with open("test_cases.json", "w") as file:
    json.dump(test_case_list, file, indent=4)

print("\n[STEP 2] Writing test cases to test_cases.json ... Done")

#STEP 3 — Read the .json file back
with open("test_cases.json", "r") as file:
    loaded_test_cases = json.load(file)

# print(loaded_test_cases)
print("\n[STEP 3] Reading test cases back from test_cases.json ... Done")
