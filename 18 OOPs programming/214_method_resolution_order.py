'''
->The MRO is the order in which Python looks for a method in a class hierarchy. It follows the left-to-right, depth-first search order.
->call .mro() method upon object.
->i.e. c->b->a if a has method show then order will be c->b->a->object(parent class by default)

->->it will show order how it is looking for method via inheritance.
->need to recall those 4 figures from lecutres.
->python folllows left to right order.

'''

class a:
    def show(self):
        print('a')
class b(a):
    pass
class c(b): #try class c (a):
    pass
c1=c()
c1.show()
print(c.mro())
'''
Method Resolution Order (MRO):
1. Definition:

MRO is the order in which Python looks for a method in a class hierarchy.
It determines the sequence in which base classes are searched when looking for a method in a class.
2. How Python Searches for Methods:

When you call a method on an object, Python looks for that method in the class of the object.
If the method is not found in the class, Python looks for it in the base classes, following the MRO.
3. Left-to-Right, Depth-First Order:

Python follows a left-to-right, depth-first order when searching for methods.
It first looks in the current class, then in the leftmost base class, and so on, until it reaches the ultimate base class (object).
4. C3 Linearization Algorithm:

Python uses the C3 linearization algorithm to determine the MRO.
It ensures a consistent and predictable order by resolving conflicts in a deterministic way.
5. Accessing MRO:

You can access the MRO of a class using the mro() method or the __mro__ attribute.
Example: print(MyClass.mro()) or print(MyClass.__mro__)
6. Example:

python
Copy code
class A:
    def show(self):
        print('A')

class B(A):
    pass

class C(B):
    pass

obj = C()
obj.show()  # Python looks for 'show' in C, B, A, and object
7. Multiple Inheritance:

In the case of multiple inheritance, MRO becomes crucial to determine the order in which base classes are searched.
The C3 algorithm helps resolve conflicts that may arise in multiple inheritance scenarios.
8. Changing MRO Explicitly:

You can influence the MRO by changing the order of base classes or using the super() function intelligently.
9. Diamond Inheritance Problem:

MRO helps resolve issues like the diamond inheritance problem in multiple inheritance scenarios.
10. Important to Understand:

Understanding MRO is crucial for dealing with complex class hierarchies and multiple inheritance scenarios.
'''