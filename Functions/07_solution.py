def sum_all(*args):
    print(*args)
    print(args)
    
    for arg in args:
        print(arg*2) 
       
    return sum(args)

print(sum_all(2, 3, 4))
