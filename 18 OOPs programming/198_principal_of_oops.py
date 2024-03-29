'''
->oops:paradigm for developing appn.(paradigm:methodology or stratergy to dev appn/style of programme)
->Encaspsulation,Abstraction,Inheritance,Polyorphism:these principals must be followed by any oop lang.
->Enc.:means combining all the related things together.
    -The path function is used to encapsulate the URL patterns.
->Abs.:means showing required features and hiding internal details.
    -in django name='index' parameter work as lelvel of abstraction.
->Inhe.: inheriting the features of existing class.
    -from djanfo.views.generic import view
->Poly.:one name and different actions .
    By using a single item we can refer multiple things together.
    for example cat and dog class is inheriting from animal class which has speak method. cat and dog object can call speak method with different output

----Continuation of lecture 199:classes vs object
->object is instance of class.it is behave by properties and attribute of class
->class is template of object. i.e blueprint of object
->
----Continuation of lecture 200:How to write a class
'''
#creaating a class of cuboid.
#When we write a variable we also need to initialise it .
#  Initialisation is done in
#  constructor (java) but in python we can write constructor method

class cuboid:
    def __init__(self,l,b,h): #if you want to make parameter optional then default argument l,b,h=1 then c1=cuboid()/cuboid(10)/cuboid(10,12)
        print(id(self))
        self.length=l #self.l/,b/,h->instance variable. self->instance reference
        self.breadth=b
        self.height=h #it is encapsulated
    def volume(self): #volume->instance method 
        return self.length*self.breadth*self.height
    def total_area(self):
        print('inside total area method',id(self))
        return 2*(self.length*self.breadth + self.breadth*self.height + self.height*self.length)    
    def lidarea(self):
        return self.length*self.breadth

c1=cuboid(10,10,10)
print(c1.lidarea(),c1.total_area(),c1.volume(),'\n\n')
c2=cuboid(1,1,1)
print('c2 id',id(c2))

#----Continuation of lecture 201:self and constructor
'''
->constructor:constructor method.when we create object automatically this will be called
->self:self is the reference to the same object
    c1.cuboid(1,1,1) When we talking about c1  self belongs to c1
    c2.cuboid(2,2,2) when we talking about c2 self belongs to c2
    c3.cuboid(3,3,3)
    when we called c1.volume(), volume method will be called, and it is taking parameter
        so what is pass there c1 itself is pass there.i.e same object is passed
'''

'''from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

my_circle = Circle(radius=5)
print(f"Circle Area: {my_circle.area()}")

An abstract base class is a class that cannot be instantiated, and it is meant to be subclassed by other classes. The Shape class declares an abstract method area, which means any concrete subclass must provide its own implementation of the area method.
'''