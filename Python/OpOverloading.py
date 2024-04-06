class Overload:
    def __init__(self):
        self.list1 = []
    def getElement(self):
        n = int(input("Enter the size of list:"))
        for i in range(n):
            ele = int(input("Enter Element:"))
            self.list1.append(ele)
    def __add__(self,other):
        newlist = []
        for i in range(len(self.list1)):
            newlist.append(self.list1[i] + other.list1[i])
        return newlist
    
    def __sub__(self,other):
        newlist = []
        for i in range(len(self.list1)):
            newlist.append(self.list1[i] - other.list1[i])
        return newlist
    
    def __mul__(self,other):
        newlist = []
        for i in range(len(self.list1)):
            newlist.append(self.list1[i] * other.list1[i])
        return newlist

    def __truediv__(self,other):
        newlist = []
        for i in range(len(self.list1)):
            newlist.append(self.list1[i] / other.list1[i])
        return newlist
    
    def __floordiv__(self,other):
        newlist = []
        for i in range(len(self.list1)):
            newlist.append(self.list1[i] // other.list1[i])
        return newlist
