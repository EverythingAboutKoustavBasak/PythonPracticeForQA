user_age = int(input("Pls Enter Age - "))
user_day = (input("pls enter day - ")).lower()

ticket_price = 12 if user_age>=18 else 8

if user_day == "wednesday":
    ticket_price = ticket_price - 2 #ticket_price -= 2

print("Your ticket price is = $", ticket_price)
    



