'''
->Creating our own error class:
    have a look at hierarchy.
    Parent class is base class then exception then arithmatic and goes on.
    better to create from inheriting exception class.
'''

'''
A constructor is a special member function in a class in object-oriented programming 
that is used to initialize the object of the class. 
It has the same name as the class and is automatically called 
when an object of the class is created. 
The primary purpose of a constructor is to set up the initial state of the object, 
which means initializing its data members 
'''

'''class MyError(Exception):
    def __init__(self, msg):
        self.msg=msg

try:
    raise MyError('this is error')
except MyError as e:
    print(e)'''

class MyError(Exception):
    def __init__(self, msg):
        self.msg=msg
    def __str__(self):
        #return self.msg
        return 'creating my exception'

try:
    raise MyError('this is error') #intialize goes into msg

except MyError as e:
    print(e)
'''
-Imagine you have a car. When you talk about your car, you might say, "My car is red." 
In this case, "my car" is like self because it refers to your specific car.
-In Python, 'self' is a reference to the instance of an object within a class. 
It allows the object to access and modify its own attributes and methods. 
Think of it as a way for the object to refer to itself,
 similar to how we say 'my car' to talk about our specific car. '
Self' helps us work with the object's data and functions within a class'''