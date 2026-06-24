
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


