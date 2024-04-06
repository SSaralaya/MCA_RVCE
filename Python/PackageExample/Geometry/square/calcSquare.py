import math as m

def area():
    side = int(input("Enter the side of square:"))
    return side * side

def perimeter():
    side = int(input("Enter the side of the square:"))
    return 4 * side

def diagonal():
    side = int(input("Enter the side of the square:"))
    return m.sqrt(2) * side
