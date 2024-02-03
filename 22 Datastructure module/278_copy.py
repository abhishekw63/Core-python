'''
->copy.copy( x ) : 
• It is known as shallow copy . 
Let us know why it is said as shallow copy 	lets take an example 		
L = [ 10 , 20 , 30 , 40 , 50 ] • If you want to copy L in L1 .
Then L1 will be holding the same object . 
• L1 will create the new list is created but it will not create objects of the L
'''
import pprint
import copy
l1=list(range(10,70,10))
print(1,l1)

l2=copy.copy(l1)
print(2,l2)
print(3,l1[0],id(l1[0]))
print(4,l2[0],id(l2[0])) #shallow copy

'''
copy.deepcopy( x )  
• This is also said as recursive copy ( copy of list then sublist than sublist than sublist …. So on ) 
• In this deep copy it will create the L1 ( list ) and it will create an object( numbers) too .
This is like real duplicate
•By this deep copy will not work for int , float , string , complex etc ….
It will works with classes , objects , functions ..
'''

class person:
    def __init__(self,name):
        self.name=name

l2=[person('raj'),person('abhi'),person('shiva')]

l3=copy.deepcopy(l2)
#pprint.pprint(l3)
print(6,l2[0],id(l2[0]))
print(7,l3[0],id(l3[0])) 
