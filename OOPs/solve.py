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


#inheritance

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) #populated from Car class
        self.battery_size = battery_size
    
electric_meta_car = ElectricCar("Tata Electric", "Meta", "Medium")
print(f"Electric Car = {electric_meta_car.brand} {electric_meta_car.model} {electric_meta_car.battery_size}")
print(f"Full name = {electric_meta_car.full_car_name()}")


        
    

