#solution no - 8 - Property decorator

'''
The @property decorator allows a method to be accessed like an attribute. 
It is commonly used to implement getters, setters, and validation while providing a clean attribute-style interface.
It is also use to create Read-Only Property
'''

   
class Car:

    def __init__(self, brand, model):
        self.brand = brand #instant variable - belongs to Object
        self.__model = model 
        
    @property
    def model(self):
        return self.__model
        
        
    
#inheritance
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model) #populated from Car class
#         self.battery_size = battery_size

            
tata_car = Car("Tata", "Nano")
# tata_car.model = "City Car"

print(tata_car.model) 
print(tata_car.model) 






        
    

