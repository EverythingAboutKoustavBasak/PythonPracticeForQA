user_number = int(input("Enter Number: "))

is_prime = True
if (user_number<=1):
    print("try again ...")
    exit()
elif(user_number>1):
    for i in range(2, user_number):
        if(user_number%i == 0):
            is_prime= False
            break
print(is_prime)

