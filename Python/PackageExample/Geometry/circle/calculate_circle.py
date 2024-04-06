import math as m

def area():
    radius = int(input("Enter the radius of the circle:"))
    a=m.pi * m.pow(radius, 2)
    return a

def circumference():
    radius = int(input("Enter the radius of the circle:"))
    c=2 * m.pi * radius
    return c
