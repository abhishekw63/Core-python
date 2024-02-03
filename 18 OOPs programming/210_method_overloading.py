'''
->Method overloading is used for achieving polymorphism.
->Python supports overloading writing one method which can act differently in different situations.
-> Python does not allow two methods using same name.
     It will try to call out the second method and shadowed the second method 
->python is having method overloading implicitly.
    We dont have to write multiple methods with the same name
    but the single method can behave in different type of method.
'''

'''class Arithmatic:
    def sum(self,x,y):
        print( x+y )
    
a1=Arithmatic()
a1.sum(10,20)
a1.sum(10.2,20.1)
a1.sum('ABhishek ','Wagh')'''

#------------------------------------


'''class Arithmatic1:
    def sum(self,x,y):
        print( x+y )
    def sum(self,x,y,z): #TypeError
        print( x+y )
a1=Arithmatic1()
a1.sum(10,20)
a1.sum(10.2,20.1)'''

#------------------------------------
class Arithmatic:
    def sum(self,x,y,z=None):
        s=x+y
        if z==None: # if z is not None:
            return print(s)
        s+=z
        return print(s)
    
a1=Arithmatic()
a1.sum(10,20,10)
