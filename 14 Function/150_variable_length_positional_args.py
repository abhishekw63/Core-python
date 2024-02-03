print('variable length arguments:')
def fun1(*args):
    print(args)

fun1()
fun1(11,12,13)
fun1(11,12,14,15)

def fun2(a,b,*args): #value before varibale argument must be positional args.
    print('before *args:',a,b,args,'.')

fun2(1,2,'A','B','C')

def fun3(*args,a,b): #value after variable keywords must be keyword args.
    print('after args:',a,b,args)

fun3('arg1','arg2','arg3',b=5,a=4)

print('-----------------------------------------')

print('unpacking arguments:')

def fun4(*args):
    print('unpacking elements:',*args)

l1=[5,6,7]
fun4(*l1) #use asterisk. you can use tuple and set also.

def fun5(a,b,c):
    print('Using indexing:',a,b,c)

l2=[7,8,9]
fun5(l2[0],l2[1],l2[2])

print('-----------------------------------------')

print('Multiple return values:')

def fun6(a,b,c):
    return a+1,b+1,c+1

x,y,z=fun6(10,20,30)
print('multiple return values:',x,y,z)
6
tup=fun6(111,22,444)
print('In tuple form:',type(tup),tup)
print('Unpacking tuple form:',*tup)

num1,num2,num4=tup
print(num1,type(num2),num4) #unpacking element of tuple.


