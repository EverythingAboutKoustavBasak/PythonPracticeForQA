import json

with open("states.json", "r") as file:
    data = json.load(file)

# print(data)
# print(type(data))

# print(data["states"])

for area in data["states"]:
    print(f"{area["name"]} ---> {area["abbreviation"]}")
    
    
#delete the area codes and write a new .json file

for area in data["states"]:
    del area["area_codes"]
    
with open("new_states.json", "w") as file2:
    json.dump(data, file2, indent=2)
    