user_password = len(input("Pasword -"))

if user_password<6:
    print("password is weak")
elif user_password>=6 and user_password<=10:
    print("password is medium")
else:
    print("password is strong")
