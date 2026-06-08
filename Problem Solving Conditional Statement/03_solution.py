user_score = int(input("Pls Enter your score: "))

if(user_score>100):
    print("Pls check the number again")
    exit()

if user_score>=90:
    grade = "A"
elif user_score>=80:
    grade = "B"
elif user_score>=70:
    grade = "C"
elif user_score>=60:
    grade = "D"
else:
    grade = "F"

print("Grade- ", grade)