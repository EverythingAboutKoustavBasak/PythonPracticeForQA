
word_to_be_searched = "learning"
with open("practice.txt", "r") as file:
    data = file.read()
    
if(data.find(word_to_be_searched) != -1):
    print("Yes the word is present")
else:
    print("Not found! ")
    