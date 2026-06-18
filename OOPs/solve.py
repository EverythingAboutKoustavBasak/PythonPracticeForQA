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
"""
Does Python support method overloading?

No, Python does not support true method overloading like Java. 
If multiple methods with the same name are defined, the last definition overrides the previous ones. 
Similar behavior can be achieved using default arguments, *args, or **kwargs.
"""
"""
A static method is a method that belongs to a class rather than an instance. It is defined using the @staticmethod decorator 
and does not receive self or cls as an argument. Static methods are typically used for utility functions related to 
the class but that do not need access to instance or class data.
"""
   
class Car:
    
    total_cars = 0      # Class Variable - belongs to Class

    def __init__(self, brand, model):
        self.brand = brand #instant variable - belongs to Object
        self.model = model
        
        Car.total_cars += 1 #Car.total_cars = Car.total_car+1
    
    def full_car_name(self):
        return (f"Full Car Name = {self.brand} {self.model}")   
    
    #polymorphism
    def fuel_type(self):
        return "Use Petrol or Desel" 
    
    #static method
    @staticmethod 
    def genaral_car_desc():
        return "Cae is a use full object"

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
print(f"tata_car is a instance of Car Class = {isinstance(tata_car, Car)}")
print(f"tata_car is a instance of ElectricCar Class = {isinstance(tata_car, ElectricCar)}")
  
electric_meta_car = ElectricCar("Tata Electric", "Meta", "Medium")
print(f"Electric Car = {electric_meta_car.brand} {electric_meta_car.model} {electric_meta_car.battery_size}")
print(f"Full name = {electric_meta_car.full_car_name()}")
print(electric_meta_car.fuel_type())
print(f"electric car is a instance of Car Class = {isinstance(electric_meta_car, Car)}")
print(f"electric car is a instance of ElectricCar Class = {isinstance(electric_meta_car, ElectricCar)}")


tata_car = Car("Tata", "SUV")

tata_car2 = Car("Tata", "Ola")

print(Car.genaral_car_desc())
# print(tata_car.genaral_car_desc()) #not possivbe beacuse tata_car is a instant and Car is a class

print(f"Total no of car {Car.total_cars}")



        
    

