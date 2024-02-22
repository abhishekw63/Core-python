'''
->function as a object.
->nested function.
->fn as a parameter.
->fn returning a fn.
'''


def fn(name=None):
    print('hello',name)

#fn('abhishek')

display=fn #function as a object proved.
display('abhishek')
print('--------------------------------')

def outer():

    def inner():    #nested function.
        print('this is inner function.')
    
    inner()

outer() 
print('------------------------------------')

def add(x,y):
    print(x+y)

def sub(x,y):
    print(x-y)

def fun(f,x,y): #function as a parameter
    f(x,y)

fun(add,10,20)
print('------------------------------------')

def outer1():
    def inner1():
        print('function returning a function.')

    return inner1

returned=outer1() #called outer1 to get inner1
returned() #called returned inner1 function








