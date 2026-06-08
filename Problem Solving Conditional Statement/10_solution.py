user_pet = input("Enter your pet - ").lower()
user_pet_age = int(input("Enter your pet age - "))
pet_food = ""

if(user_pet=='dog' and user_pet_age<2):
    pet_food="Puppy food"
if(user_pet=="cat" and user_pet_age>5):
    pet_food="Senior cat food"
else:
    pet_food = "Out of stock! "
print(user_pet+" is your pet and age is "+str(user_pet_age)+" eat - "+pet_food)
