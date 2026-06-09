user_multiplication_number = int(input("pls enter number for multiply= "))

for i in range(1, 11):
    if(i==5):
        continue
    print(user_multiplication_number, " X ", i, " = ", user_multiplication_number*i)
    