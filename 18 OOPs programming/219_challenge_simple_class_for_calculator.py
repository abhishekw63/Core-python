class Calc:
    @staticmethod
    def add(x,y):
        return x+y
    
    @staticmethod
    def sub(x,y):
        return x-y
    
    @staticmethod
    def mul(x,y):
        return x*y
    
    @staticmethod
    def div(x,y):
        return x/y
    
print(Calc.add(5,7))
print(Calc.div(40,3))
'''
In Python, methods within a class are, by default, instance methods. 
This means they operate on an instance of the class and 
have access to the instance's attributes.
 To make a method a static method, 
 which is not bound to the instance of the class, 
 the `@staticmethod` decorator is used.

Here's a breakdown:

1. **Instance Method (Default):**
   ```python
   class MyClass:
       def instance_method(self, x, y):
           return x + y

   obj = MyClass()
   print(obj.instance_method(5, 7))
   ```

   In this case, `instance_method` is an instance method, and you need to create an object (`obj`) to call it.

2. **Static Method (Using `@staticmethod`):**
   ```python
   class MyClass:
       @staticmethod
       def static_method(x, y):
           return x + y

   print(MyClass.static_method(5, 7))
   ```

   With the `@staticmethod` decorator, `static_method` becomes a static method. You can call it on the class itself, without creating an instance.

   ```python
   MyClass.static_method(5, 7)
   ```

So, the `@staticmethod` decorator is used
 explicitly to define static methods. 
 Without it, the method would be treated as an instance method.
Using the decorator makes the code clearer and 
follows a more explicit approach, especially when reading or maintaining the code.
'''