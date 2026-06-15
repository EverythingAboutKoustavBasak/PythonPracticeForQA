def factorial(num):
    if(num==1):
        return 1
    return num*factorial(num-1)

print(f"Factorial of Number = {factorial(5)}")

def sum(num):
    if(num==1):
        return 1
    return num+ sum(num-1)

print(f"Sum of Number: {sum(5)}")



