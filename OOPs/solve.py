# class Car:
#     brand = None
#     model = None
    
#     #constructor  - self = this (key word)
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
 
 
#best Practice - Usually, don't declare instance variables at the class level if they will be initialized in __init__.   
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_car_name(self):
        return (f"Full Car Name = {self.brand} {self.model}")
        
            
tata_car = Car("Tata", "Nano")
print(f"Tata Car Brand= {tata_car.brand}")
print(f"Tata Car Model= {tata_car.model}")
print(tata_car.full_car_name())

