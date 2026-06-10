User_List_unmber = int(input("Pls Enter how much char you want to add in the list = "))
user_list = []

for i in range(User_List_unmber):
    user_input_char = input("Pls enter char #"+str(i+1)+" = " ).lower()
    user_list.append(user_input_char)

print("List = ", user_list)


#time comlexcity - high O(n^2)
for item in user_list:
    if(user_list.count(item)>1):
        print("duplicate Iteam is", item)
        print("Number of char occurence", user_list.count(item))
        break
 
 
#less time complexity O(n)   
# seen = set()

# for item in user_list:
#     if item in seen:
#         print(item)
#         break

#     seen.add(item)