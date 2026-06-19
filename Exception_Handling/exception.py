try:
    age = int(input("Enter age = "))
    print("age ", age)
    list = [2,4,5]
    print(list[age])
# except Exception as e:
#     print(e)

except ValueError:
    print("Input Wrong Value!")  
except IndexError:
    print("Index Out of bounr or maybe wrong pls check")
    
finally:
    print("Always Executed")

