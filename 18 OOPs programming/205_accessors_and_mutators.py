'''
->These are the types of methods that can be written inside any class.
->Accessor methods are useful for reading the property of a class of an object.
->Mutator is used for writing and updating properties of class and its objects.
->So these methods can be called as reading and writing methods
->These methods are followed by object oriented programming
->it is like getter and setter function of cpp

'''

class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        print(self.length*self.breadth)
    def GetLength(self):
        print(self.length)
    def SetLength(self,len):
        self.length=len

r1=rectangle(2,3)
r1.GetLength()

r1.SetLength(3)
r1.area()