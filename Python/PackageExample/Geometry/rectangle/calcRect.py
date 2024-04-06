import math as m

def area():
    length = int(input("Enter the length of the rectangle:"))
    breadth = int(input("Enter the breadth of the rectangle:"))
    return length * breadth

def perimeter():
    length = int(input("Enter the length of the rectangle:"))
    breadth = int(input("Enter the breadth of the rectangle:"))
    return 2 * (length + breadth)

def diagonal():
    length = int(input("Enter the length of the rectangle:"))
    breadth = int(input("Enter the breadth of the rectangle:"))
    return m.sqrt((length * length) + (breadth * breadth))