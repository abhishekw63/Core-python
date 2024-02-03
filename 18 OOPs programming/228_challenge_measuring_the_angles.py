'''
->OPERATOR OVERLOADING.
'''

class Angle:
    def __init__(self,deg):
        self.degree=deg
    
    def __add__(self,other):
        #sum=self.degree+other.degree
        '''
        ->You're overloading the + operator,
        but the result is just a numerical sum of degrees,
        not an object of the Angle class.
        Operator overloading is more powerful
        when it allows you to work with objects of the same class, 
        creating a meaningful and context-specific result.
        '''
        sum=Angle(self.degree+other.degree)
        return sum
    
    def __str__(self):
        return(f'Degree is {str(self.degree)}')

a1=Angle(40)
a2=Angle(30)

print(a2) 

#print(a1.__add__(a2))
#print(a1+a2)

a3=a1+a2
print(a3)

'''
->The __add__ method returns a new Angle object, 
representing the sum of angles. 
This aligns more closely with the idea of operator overloading, 
where the + operator is used to add two objects of the same class, 
and the result is also an object of the same class, 
allowing for a more intuitive and object-oriented design.

->So, while your program does demonstrate operator overloading by allowing the use of the + operator with Angle objects, 
your tutor's implementation takes it a step further by returning a new Angle object as the result.
'''