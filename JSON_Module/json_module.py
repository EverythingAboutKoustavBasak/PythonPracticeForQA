"""
Python dictionaries can be converted to JSON using json.dumps() 
and JSON can be converted back to dictionaries using json.loads().
--------------------------------------------------------
dict  -> json.dumps() -> JSON
JSON -> json.loads() -> dict
----------------------------------------------------------
json.load() → Reads JSON from a file and converts it to a Python object (usually a dict).
json.loads() → Reads JSON from a string and converts it to a Python object.
json.dump() → Writes a Python object to a JSON file.
json.dumps() → Converts a Python object to a JSON string.
------------------------------------------------------
JSON String                                         
      |
      | loads()
      v
Python Dict
      |
      | dumps()
      v
JSON String
----------------------------------------------------
JSON File
      |
      | load()
      v
Python Dict
      |
      | dump()
      v
JSON File
----------------------------------
NB-
JSON does not understand:True, False, None
It uses : true, false and null


"""
import json

data1 = '{ "Name" : "Koustav", "Role" : "SDET" }'

#conver JSON to dict
dict_json = json.loads(data1)
print(dict_json)
print(dict_json["Name"])
print(type(dict_json))



#convert jsonfile to dict

'''
open("employee.json", "r") that means open the file which name is "emp.json" in 'r' mode means read mode
'with'- with automatically closes the file after use.

with out "with" it should be like - 
file = open("employee.json", "r")
# work
file.close()
'''

with open("emp.json", "r") as file1:
    data2 = json.load(file1)

print(data2) 
print(data2['Emp_Role']) 
print(type(data2))

print("________________________________________________________________________")
data3 = {"Name": "Sonai", "Skill": ["Java", "Selenium", "TestNG"], "Role": ("SDET", "Automation Eng", "Tester"), "Is-Open": True}
print(type(data3))

example1 = json.dumps(data3)
print(type(example1))
print(example1)
print("________________________________________________________________________")


#write thr data3 as json file
with open("empn.json","w") as file2:
    file2 = json.dump(data3, file2)
