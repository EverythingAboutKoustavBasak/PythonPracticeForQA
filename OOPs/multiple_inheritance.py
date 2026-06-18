class Car:
    
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model

class Engine:
    
    def engine_info(self):
        return "This is Engine Class"
    
class Battery:
    
    def Battery_info(self):
        return "This is Battery Class"
    
class EtectricCar(Car, Battery, Engine):
    pass


electric_car = EtectricCar("Tata", "Meta")
print(electric_car.Battery_info())
print(electric_car.engine_info())
