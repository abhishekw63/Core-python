'''
->Method Overriding.
'''
import math
class Shape:
    def __init__(self,name):
        self.s_name=name
    def area(self):
        print(f'Area of shape is:{None}')

class Circle:
    def __init__(self,rad):
        self.radius=rad
    
    def area(self):
        print(f'Area of circle is {math.pi * (self.radius **2)}')

class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    
    def area(self):
        print(f'Area of rectangle is {self.length * self.breadth}')


s1=Shape('raja')
s1.area()

c1=Circle(7)
c1.area()

r1=Rectangle(1,3)
r1.area()
    