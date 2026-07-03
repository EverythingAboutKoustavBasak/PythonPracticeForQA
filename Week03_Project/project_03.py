import json
import requests


test_case_list=[]
post_test_case_success_count = 0
post_test_case_failed_count = 0

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
    # if test_case_create["status"] == "passed":
    #     test_case_passed_count += 1
    # elif test_case_create["status"] == "failed":
    #     test_case_failed_count += 1
        
    #add the test cases to the lists
    test_case_list.append(test_case_create)
    
# print(test_case_list)


   
# Step 2 — Write test cases to a .json file
with open("test_cases.json", "w") as file:
    json.dump(test_case_list, file, indent=4)

print("\n[STEP 2] Writing test cases to test_cases.json ... Done")

#STEP 3 — Read the .json file back
with open("test_cases.json", "r") as file:
    loaded_test_cases = json.load(file)

# print(loaded_test_cases)
# print(type(loaded_test_cases))
# print(loaded_test_cases)
print("\n[STEP 3] Reading test cases back from test_cases.json ... Done")




#step 4 - Posting test cases
# step-5 update the result


print("\n[STEP 4] Posting test cases to JSONPlaceholder API...")
print("=============================================")
print("            POSTING REPORT                     ")
print("=============================================")


url = "https://jsonplaceholder.typicode.com/posts"

header_content = {
            "Content-Type": "application/json"
}

for index, test_case in enumerate(loaded_test_cases, start=1):


    api_status_sent = ""
    try:
        res = requests.post(url, 
                            headers=header_content, 
                            json=test_case
                            )
        
        response_data = res.json()
        
        
        
        if res.status_code==201:
            api_status_sent = "Request Sent Successfully to Server"
            post_test_case_success_count+=1
        else:
            api_status_sent = "Request not sent Server Issue"
            post_test_case_failed_count+=1
        
        print(f"\nTest Case# {index}         : {test_case['title']}")
        print(f"API Status Sent      : {api_status_sent}")
        print(f"API Status Code      : {res.status_code}")
        print(f"API Generated ID     : {response_data['id']}")
        print("-" * 55)
        
        
    except requests.exceptions.RequestException as e:
       post_test_case_failed_count += 1       
       print(f"\nTest Case {index}: {test_case['title']}")
       print(f"Error            : {e}")                    # print the actual error
       print("-" * 55)
       continue
        
    
    # print(res.status_code)
    # print(res.text)
    
#total count result
print("==============================================================")
print(f"Total Posted = {len(loaded_test_cases)} | Req Success = {post_test_case_success_count} | Req Failed = {post_test_case_failed_count}")
print("==============================================================")


#end
print("Made By KOUSTAV BASAK - Thank you for using!!!")