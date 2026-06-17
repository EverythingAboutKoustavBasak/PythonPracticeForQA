# class Car:
#     brand = None
#     model = None
    
#     #constructor  - self = this (key word)
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
 
 
#best Practice - Usually, don't declare instance variables at the class level if they will be initialized in __init__.

'''
Interview Point

Java has two types of polymorphism:

Compile-time Polymorphism
Method Overloading
Same method name, different parameters
Runtime Polymorphism
Method Overriding
Inheritance + same method name

Python mainly achieves polymorphism through:

Method overriding
Default parameters
*args and **kwargs
'''

   
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_car_name(self):
        return (f"Full Car Name = {self.brand} {self.model}")   
    
    #polymorphism
    def fuel_type(self):
        return "Use Petrol or Desel" 

#inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) #populated from Car class
        self.battery_size = battery_size
    
    #polymorphism
    def fuel_type(self):
        return "Use Electric Battery" 
            
tata_car = Car("Tata", "Nano")
print(f"Tata Car Brand= {tata_car.brand}")
print(f"Tata Car Model= {tata_car.model}")
print(tata_car.full_car_name())
print(tata_car.fuel_type())
  
electric_meta_car = ElectricCar("Tata Electric", "Meta", "Medium")
print(f"Electric Car = {electric_meta_car.brand} {electric_meta_car.model} {electric_meta_car.battery_size}")
print(f"Full name = {electric_meta_car.full_car_name()}")
print(electric_meta_car.fuel_type())




        
    

