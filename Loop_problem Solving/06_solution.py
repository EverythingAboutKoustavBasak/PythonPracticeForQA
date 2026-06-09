user_fact_no = int(input("give the number = "))
factorialnum = 1
if (user_fact_no==0):
    print("factorial = 1")
    exit()
    
while user_fact_no > 0:
    factorialnum =  factorialnum*user_fact_no
    user_fact_no=user_fact_no-1
    
print("Factorial = ", factorialnum)
