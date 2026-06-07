test_types_dict = {
    "Initial": "Smoke Test",
    "Second Round": "Sanity Test",
    "Third Round": "Retesting"
}

print(test_types_dict)

print(test_types_dict["Initial"])
print(test_types_dict.get("Second Round"))

for key in test_types_dict:
    print(key)

for key in test_types_dict:
    print(key, test_types_dict[key])

for key, value in test_types_dict.items(): #use 2 variable in for loop and ittarate all the emelemtes one by one 
    print(key, value)

#conditional statement
if "Second Round" in test_types_dict:
    print("We have 2nd statge in test plan as sanity")

print("Total length of test types- ", len(test_types_dict))

#add test type in the dict
test_types_dict["Fourth Round"]="Regression Testing"
print("New Test Type - ", test_types_dict)

#delet
test_types_dict.pop("Second Round")
print(test_types_dict)

del test_types_dict["Fourth Round"] 
print(test_types_dict)

test_types_dict.popitem() #remove the last key/value fro the dict
print(test_types_dict)

#add item in the dict
test_types_dict["Second Round"] = "Sanity Testing"
test_types_dict["Third Round"] = "Retesting"
print(test_types_dict)

test_types_dict_copy = test_types_dict.copy()
print(test_types_dict_copy)


#nested dict
testing_Category ={
    "functional Testing":{
        "1st Round":"Smoke Test",
        "2nd Round": "Sanity Test"
    },
    "non-functional Test":{
        "3rd Round": "Performance Test",
        "4th Round": "Security Test"
    }
}

print(testing_Category)
print(testing_Category["non-functional Test"]["3rd Round"])



squre_num = {x:x**2 for x in range(5)}
print(squre_num)

#clear whole dict
print(squre_num.clear())

#lists
testing_round = ["1st", "2nd", "3rd"]
default_value = "Testing"
#creating set from the above 2 list
new_test = dict.fromkeys(testing_round, default_value)
print(new_test)

