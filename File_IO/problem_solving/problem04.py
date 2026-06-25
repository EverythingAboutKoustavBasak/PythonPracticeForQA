"""
read() → Read everything.
readline() → Read one line.
readlines() → Read all lines into a list.

"""

def find_line_of_word(userInput):
    data = True
    line_number = 1
    with open("practice.txt", "r") as file:
        
        while data:
            data = file.readline()
            if(data.find(userInput) != -1): #if(userInput in data):
                return line_number 
            
            line_number+=1
    
    return -1
line_number = find_line_of_word("Python")
print(line_number)
            
            
            
    
    
    
        