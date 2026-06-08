user_distance = int(input("Enter Distence in Km = "))

if user_distance<3:
    print("Walking")
elif user_distance>=3 and user_distance<=15:
    print("Bike")
else:
    print("Car")
