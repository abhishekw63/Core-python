'''
->Polymorphism means One name different actions
->Polymorphism allows objects of different types to be treated as objects of a common type.
    In your example, both Dog and Penguin classes have a talk method, and they are both passed to the petlover function.

->duck typing
    Duck typing is a concept where the  class of an object is less important than the methods and properties it defines.
    In your case, the petlover function doesn't care about the specific type of the pet object; it only cares that it has a talk method
    
->method overloading
->method overriding
->Operator Overloading
'''
def petlover(pet_obj):
    pet_obj.talk()
    if not hasattr(pet_obj,'run'):
        return print('Run method is not available')
    pet_obj.run()
    
class Dog:
    def talk(self):
        print(f'Dog can talk')
    def run(self):
        print('Dog can run')

class Penguin:
    def talk(self):
        print('Penguin can talk')

d1=Dog()
petlover(d1)

p1=Penguin()
petlover(p1)