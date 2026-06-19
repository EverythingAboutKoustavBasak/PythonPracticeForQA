class NotValidInputException(Exception):
    pass
try:
    
    input_user = int(input("Pls Enter number b/w 2 to 10 = "))

    if input_user<2 or input_user>10:
        raise NotValidInputException("Pls Enter number b/w 2 to 10! chack again")

except NotValidInputException as e:
    print(e)
    
    


    
    