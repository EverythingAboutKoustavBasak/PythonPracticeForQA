user_number = int(input("Enter Upto Number = "))
total_sum_of_even_number = 0

for i in range(1, user_number+1):
    if(i%2==0):
        total_sum_of_even_number = total_sum_of_even_number+i
        
print("Total sum of even number upto "+str(user_number)+" is = ", total_sum_of_even_number)

