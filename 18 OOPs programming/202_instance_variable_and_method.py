'''
->self.xyz is the instance variable. you can give any name
     Self is not a keyword  it can be anything. 
     The first we are writing is constructor is 
     called as (instance variable)
    We can give anytime instead of self
    
->if method is accessing instance variable(self) then that method becomes instance method
->if method is accessing class/static varibale then that method becames classmethod. it is define by @classmethod decorator.
->if method is not accessing any instance variable or class variable then that method becames staticmethod. it is defined by staticmethod decorater.

In python there are different types of variables and methods:
    Variables: Instance variable  Static/class variable
    Methods:  Instance method  Class method  Static method
'''

class test:
    def __init__(self):
        self.a=10
    def fun(self):
        self.b=20
     
t1=test()
print(dir(t1)) #it will have one instance variable that is 'a'
t1.c=30 #declare and intialise instance variable outside init i.e outside class
print(dir(t1)) #a c and instance method 'fun' but wont have instance variable 'b'
t1.fun()
print(dir(t1)) #now 'b' will be there.
