'''
-Immutable and mutable datastructure:
In the context of data structures like lists, sets, tuples, and dictionaries in Python, the term "immutable" refers to whether the elements or the structure of the data structure can be changed after it has been created.

Immutable Data Structures:

Tuple: Tuples are immutable. Once you create a tuple, you cannot change its elements or their order.

Mutable Data Structures:

List: Lists are mutable. You can change their elements, add or remove elements, and modify the structure of the list.

Set: Sets are mutable. You can add or remove elements from a set after its creation.

Dictionary: Dictionaries are mutable. You can add or remove key-value pairs and modify existing values.

In summary:
Immutable data structures (like tuples) do not allow modifications after creation.
Mutable data structures (like lists, sets, and dictionaries) allow modifications after creation.
'''

'''
-Map function:
The map() function takes each element from the iterable(s) and applies the specified function to it, producing a new iterable with the results.

-Zip function:
The zip() function in Python is a built-in function that takes two or more iterables as arguments and returns an iterator that produces tuples by aggregating corresponding elements from the input iterables.

''' 

'''
-Types of inheritance:
Used to acquire feautures of base class.
In Python, inheritance is a way to create a new class that inherits attributes and methods from an existing class. There are several types of inheritance in Python:

Single Inheritance:
In single inheritance, a class is derived from only one base class. The derived class inherits the attributes and methods of the base class.

class BaseClass:
    # Base class definition

class DerivedClass(BaseClass):
    # Derived class inherits from BaseClass
    
    
Multiple Inheritance:
Multiple inheritance allows a class to inherit attributes and methods from more than one base class. The derived class can access members of all the base classes.

class BaseClass1:
    # Base class 1 definition

class BaseClass2:
    # Base class 2 definition

class DerivedClass(BaseClass1, BaseClass2):
    # Derived class inherits from both BaseClass1 and BaseClass2
    
Multilevel Inheritance:
In multilevel inheritance, a class is derived from another derived class. This creates a chain of inheritance.

class Grandparent:
    # Grandparent class definition

class Parent(Grandparent):
    # Parent class inherits from Grandparent

class Child(Parent):
    # Child class inherits from Parent
    
Hierarchical Inheritance:
Hierarchical inheritance involves one base class and multiple derived classes. Each derived class inherits from the same base class.

class BaseClass:
    # Base class definition

class DerivedClass1(BaseClass):
    # Derived class 1 inherits from BaseClass

class DerivedClass2(BaseClass):
    # Derived class 2 inherits from BaseClass
    
Hybrid (or Mixed) Inheritance:

Hybrid inheritance is a combination of two or more types of inheritance. It is a mix of any two or more of the above types of inheritance.

class BaseClass:
    # Base class definition

class DerivedClass1(BaseClass):
    # Derived class 1 inherits from BaseClass

class DerivedClass2(DerivedClass1):
    # Derived class 2 inherits from DerivedClass1

'''

'''-Positional Vs Keyword arguments:
In Python, function arguments can be passed in two main ways: positional arguments and keyword arguments.

Positional Arguments:
Positional arguments are passed to a function based on their position or order in the function signature.
The order and number of positional arguments must match the function definition.
They are specified during the function call without explicitly mentioning the parameter names.

Keyword Arguments:
Keyword arguments are passed to a function by explicitly mentioning the parameter names along with their values.
The order of keyword arguments can be different from the function definition.
They allow you to specify values for specific parameters regardless of their position.

keyword shoul be on right side. that is positional argument must not be followed by keyword arg
'''

'''-Variable length arguments
*Arbitrary Positional Arguments (args):
The *args syntax allows a function to accept any number of positional arguments. These arguments are collected into a tuple.
The name args is a convention; you can use any name after the *.
def sum_values(*args):
    total = 0
    for value in args:
        total += value
    return total

result = sum_values(1, 2, 3, 4)

**Arbitrary Keyword Arguments (kwargs):

The **kwargs syntax allows a function to accept any number of keyword arguments. These arguments are collected into a dictionary.
The name kwargs is a convention; you can use any name after the **.

def print_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_values(name="John", age=30, city="New York")
'''

'''-Generator and iterator:
When you use yield inside a function, it becomes a generator.
The function returns a generator object, and its state is 
preserved between function calls. Each time you iterate over the generator, 
the function's execution is paused and resumed, and 
it continues from where it left off, producing values one at a time. 
This is useful for creating sequences of values without having to store them in memory all at once. 
Generators are memory-efficient and can be iterated lazily.

An iterator in Python is an object that allows you to iterate over a sequence of elements, one at a time, without having to know the underlying details of the sequence's structure. Iterators are implemented using two methods: __iter__() and __next__().

'''

'''

'''