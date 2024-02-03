'''
->Anonymous function
->Single line expression
->Any number of argument
'''

k=lambda miles:1.6 * miles
print('miles to km',k(1))

p=lambda a,b:a if a>b else b
print('max from 2:',p(100,20))