user_coffee_order = int(input("Coffee Order - "))
user_coffee_option = input("cofee type - ").lower()

if user_coffee_option=="extra shot":
    print("Coffee size "+ str(user_coffee_order)+" with category "+user_coffee_option)
else:
    print("make choice again to see your coffe size")