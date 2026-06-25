import os



print("----------Read File-------------------")
file1 = open("demo.txt", "r")
file_output = file1.read()
print(file_output)
file1.close()

print("----------Write File(Overrite full file)-------------------")
file2 = open("demo1.txt", "w")  
file_write = file2.write("Hola !")
file2.close()


print("----------Write File(appande only)-------------------")
file3 = open("demo1.txt", "a")  
file_write = file3.write("Koustav This side ")
file3.close()

print("----------Read File with syntax-------------------")
with open("demo2.txt", "r") as file4:
    data = file4.read()
print(data)


print("----------Write File with syntax-------------------")
with open("demo2.txt", "w") as file5:
    file5.write("\n Hi")
    
print("----------Delete file-------------------")
#need to import os module to delete any file
os.remove("demo2.txt")

print("file deleted !!")