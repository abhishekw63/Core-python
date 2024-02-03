'''
-> When we declare a variable inside a class but outside any method, it is called a class variable in Python.
->self.length and self.breadth are instance variables specific to each instance of the class.
->Class variables can be accessed from within the class using cls.ClassVariable, ClassName.ClassVariable, or instance.ClassVariable.
->There are two ways of accessing class variables from inside class method- 
    cls.ClassVariable  ClassName.ClassVaraiable 
->There is only one way to access class variables from stac method- •ClassName.ClassVariable 
'''
# Increment the count class variable each time a new instance is created. cuboid.count += 1

class cuboid:
    count=0 #static/class variable
    def __init__(self,l=1,b=1,h=1): 
        self.length=l 
        self.breadth=b
        self.height=h
        cuboid.count+=1 #instance variable

    def volume(self): 
        return self.length*self.breadth*self.height
    def total_area(self):
        return 2*(self.length*self.breadth + self.breadth*self.height + self.height*self.length)    
    def lidarea(self):
        return self.length*self.breadth
    @classmethod
    def counting_instance(cuboid): #It's a class method because it takes the class as its first parameter.
        print(cuboid.count) #can give cls instead of cuboid

c1=cuboid() ## Accessing the class variable using an object (c1) indicates that the class variable is shared among all instances.
c1.counting_instance()

print(cuboid.count)

c2=cuboid()
print(cuboid.count)

c3=cuboid()
c3.counting_instance() 

c1.counting_instance() #accessing using obj c1 that means class variable is common for every obj. class is sharing its copy of count

'''
When a variable is declared outside any method 
but inside the class, it is generally referred to 
as a "class variable" or "static variable."
 This variable is shared among all instances of the class.

However, if you initialize or modify this variable 
inside the __init__ method, which is called
 when creating an instance of the class, 
 it becomes an "instance variable" specific to each instance.
'''