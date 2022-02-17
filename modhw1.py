from math import pi


# To calculate the square footage of the house
def sq_house():
    width = int(input("Enter the width of your house "))
    length= int(input("Enter the length of your house "))
    area = width * length
    return f'The square footage of your house is {area}'

print(sq_house())

