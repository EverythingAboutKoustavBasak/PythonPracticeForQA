test_types = ["Smoke", "Sanity", "Regression", "Exploratory"]
print(test_types)
print(test_types[1])
print(test_types[1:3]) 
print(test_types[1:4:2]) #last value is for hopping

test_types[3]="Retesting"
print(test_types)
for n in test_types:
    print(n)
    
for n in test_types:
    print(n, end="**")
    print()
    
if "MonkeyTest" in test_types:
    print("We have this test Category - Smoke")

test_types.append("MonkeyTest") #add value in list at last
print(test_types)

if "MonkeyTest" in test_types:
    print("We have this test Category - MonkeyTest")

test_types.pop() #delete last section from list
print(test_types)

test_types.remove("Smoke") #remove pirticular value
print(test_types)

test_types.insert(1, "LocalizationTest") #insert value at pirticular section
print(test_types)


test_types_copy = test_types.copy() 
print(test_types_copy)

test_types_copy.append("Shift Left Testing")
print(test_types_copy)
print(test_types)


test_types_copy2 = test_types
test_types.append("End to End Testing")
print(test_types)
print(test_types_copy2)


#list comprihension - loop and range
cube_num = [x**3 for x in range(5)]
print(cube_num)


