user_number_list = []
positive_number_count = 0

user_count_of_List_Elements = int(input("Enter the number of List elements - "))

for i in range(user_count_of_List_Elements):
    user_num = int(input("Enter number #" + str(i+1) + ": "))
    user_number_list.append(user_num)
    
print("List = ", user_number_list)

for i in user_number_list:
    if i>0:
        positive_number_count = positive_number_count+1


print("Total +ve number in the list = ", positive_number_count)