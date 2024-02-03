'''
->Inheritance is acquiring features in a (derived)class from an existing (base) class.
->The main advantage of Inheritance is reusability of code.
->Base Class:'object' In Python, object is the base class for all classes.
    It is the root of the class hierarchy.
    Even if you don't explicitly mention it,
    your class is implicitly a subclass of object.
    ->object provides some basic methods that are inherited by all classes, such as __init__, __str__, __eq__, and others
    ->Implicit Inheritance:
        class MyClass: #If you define a class without explicitly specifying a superclass, it implicitly inherits from object.
        pass
    ->Direct Inheritance:
        class MyClass(object):#You can also explicitly inherit from object:
        pass
    ->Indirect Inheritance:
        class MyBaseClass(object):
        pass
        class MyDerivedClass(MyBaseClass): 
        pass
        #If a class explicitly inherits from another class,
        and that class inherits from object, 
        your class indirectly inherits from object.
'''
#----------------Continuation of lec 207 Constructors in inheritance
class Rectangle(object):
    def __init__(self,l,b): 
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth

class Cuboid(Rectangle):
    def __init__(self,cuboid,h):
        self.height=h

    '''def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height'''

    def volume(self):
        return self.length*self.breadth*self.height
    
c1=Cuboid(10,10,10)
print(c1.volume())
#programme wont run-> chatgpt suggesting commented init of base class.solution? below
'''
->#if you are writting constructor for a 
   derived class then the base class constructor will no be called automatically.
   if i am creating a object of derived class then the constructor of only derived class will be called not of parent class
   this things happen in cpp/java.
   so we have to called it mannually
   ->
        def __init__(self,l,b,h):
            super().__init__(l,b)
            self.height=h
'''