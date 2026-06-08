user_fruit = input("Pls enter the fruit name(eg. Banana) - ").lower()
user_fruit_color = input("Pls enter the color of the fruit: ").lower()

if user_fruit =="banana":
    if user_fruit_color == "green":
        print("Unripe fruite")
    elif user_fruit_color == "yellow":
        print("Ripe fruite")
    elif user_fruit_color == "brown":
        print("Overripe fruite")
else:
    print("Pls enter right fruite name!!!")
