import math

def circle_stat(radius):
    area = math.pi * (radius**2)
    circumference = 2 * math.pi * radius
    
    return area, circumference

area, cir = circle_stat(5)

print(f"Area = {area} squre unit and Circumference {cir} unit")
print(f"Area = {area:.2f} squre unit and Circumference {cir:.2f} unit")