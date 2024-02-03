'''
->Redefining the method of parent class in child class is said as method overriding.
->In other words, the child class has access to the properes and funcons of the parent class method while also extending addional funcons of its own to the method.
'''

class Nokia:
    def home(self):
        print('Home button is pressed')

class n73(Nokia):
    def home(self):#override method
        print('home is touched')
    
    def parent_home(self):
        super().home()

m1=n73()
m1.home()
#m1.super().home() #wont work
m1.parent_home()
