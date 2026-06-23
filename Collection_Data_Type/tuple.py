# list - mutable
#tuple - immutable - tuple object does not support items assignment

test_type = ("Smoke", "Sanity", "End to End")
print(test_type)
print(test_type[0])
print(test_type[-1])

more_test_type = ("Retesting", "Localization Testing")

all_test_type = test_type + more_test_type
print(all_test_type) 

#number of occurance - the value in the tuple
print(more_test_type.count("Retesting")) 

print(type(more_test_type))

