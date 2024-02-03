'''
->we really dont need parent class except sharing among derived class inherited from parent classs.i.e share the contents of it
->if body is not there then it is abstract class
'''
# Refer pdf its imp

import abc
#from abc import abc,abstractmethod bari shows this

class Parent(abc.ABC):
   
    def show(self):# abstractmethod
        pass
    def display(self):
        print('parent display')

class Child(Parent):
    pass
    def show(self): #try write only pass
        print('show from child')

c=Child()
c.show()
c.display()
