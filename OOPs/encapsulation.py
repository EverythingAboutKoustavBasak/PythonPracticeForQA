#solution-6
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def set_brand_value(self, brand):
        self.__brand = brand
        
    def get_brand_value(self):
        return self.__brand
    
tata_car = Car("Tata", "Nano")
# print(tata_car.__brand)
print(tata_car.get_brand_value())
print("After set the brand name ")
tata_car.set_brand_value("Tesla")
print(tata_car.get_brand_value())
"""
Python uses name mangling, not true privacy. A variable named __brand is internally renamed to _ClassName__brand. 
This prevents accidental access and naming conflicts, but it can still be accessed if someone intentionally uses the mangled name.

That's what people mean when they say Python's "private" members are only conventionally private, 
not strictly private like Java's private fields.

print(tata_car._Car__brand)
"""

 
    
        
        
        
    