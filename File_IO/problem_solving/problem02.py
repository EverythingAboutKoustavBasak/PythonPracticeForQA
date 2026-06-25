with open("practice.txt", "r") as file:
    data = file.read()

print(f"Before replace Java to Python:\n{data}")

new_data = data.replace("Java", "Python")
with open("practice.txt", "w") as file2:
    file2.write(new_data)
   