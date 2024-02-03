'''
->achieving polymorphism
->dependent on object
'''
class Cat:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    def info(self):
        print(f'My name is {self.name} and age is {self.age}')

    def sound(self):
        print('Mew Mew')

class Dog:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    def info(self):
        print(f'My name is {self.name} and age is {self.age}')

    def sound(self):
        print('Bow Bow')
    
def pet(pet_obj): #global function
    pet_obj.info() 
    pet_obj.sound()

c1=Cat('Kitty',5)
pet(c1)

d1=Dog('Sheru',4)
pet(d1)