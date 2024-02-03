#variable length keyword arguments

def fun1(**kwargs):
    print(kwargs) #it will print dictionary.
    print(type(kwargs))

fun1(a=10,b=20,c=30,d=40)

def fun2(a,b,*pargs,c=0,**kwargs):  #a and b should be positional and c must be keyword.
    print(kwargs,c,pargs,a,b)

fun2(10,20,3,4,5,6,7,d=90,e=100,f=110,g=120,h=130)
