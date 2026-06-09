user_str = input("Give a String = ")

for i in user_str:
    if user_str.count(i)>1:
        print("first repetaive char is ", i)
        break

