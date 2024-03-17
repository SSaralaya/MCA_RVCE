from OpOverloading import *
obj1 = Overload()
obj2 = Overload()
obj1.getElement()
obj2.getElement()
f =1
while(f):
    print("\nMenu \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Floor Division \n6.Exit")
    ch = int(input("Enter your choice:"))
    if(ch == 1):
        print("Result:",obj1 + obj2)
    elif(ch == 2):
        print("Result:",obj1 - obj2)
    elif(ch == 3):
        print("Result",obj1 * obj2)
    elif(ch == 4):
        print("Result:",obj1 / obj2)
    elif(ch == 5):
        print("Result:",obj1 // obj2)
    elif(ch == 6):
        f=0
    else:
        print("Invalid Choice")




