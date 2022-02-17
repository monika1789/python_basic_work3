
from math import pi

# calculate circumference of circle

def circum():
    radius = int(input("Enter the radius of the circle "))
    circumference = 2 * pi * radius
    return circumference

print(circum())