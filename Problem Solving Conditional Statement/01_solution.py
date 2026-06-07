user_age = int(input("User Age: "))

if user_age<13:
    print("Clild")
elif user_age<20:
    print("Teenager")
elif user_age<60:
    print("Adult")
elif user_age<107:
    print("Scenior")
else:
    print("Pls chekck your age again and enter right value")
    exit
