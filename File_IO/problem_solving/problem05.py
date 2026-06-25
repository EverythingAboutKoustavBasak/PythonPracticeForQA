#with split method from scratch
even_count = 0
with open("number.txt", "r") as file:
    data = file.read()
    # print(data) 
    # print(type(data)) 
number_list = data.split(",")
# print(number_list)
# print(type(number_list))
for item in number_list:
    if(int(item)%2 == 0):
        even_count += 1

print(even_count)




    
    
