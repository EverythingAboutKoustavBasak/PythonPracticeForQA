def f1(num):
    def f2(num2):
        return num2**num
    return f2

result1 = f1(2)
print(f"Result : {result1(5)}")
result2 = f1(3)
print(f"Result : {result2(5)}")
