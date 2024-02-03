gbl=10

def fun(a,b):
    lcl=a+b
    #gbl=gbl+5 #unbound local error. fun can only access and read global variable. cant modify them.
    global gbl
    g=gbl+5
    print(lcl)
    print('inside_fun:',g)

print('outside:',gbl)
#print(lcl) #inside f. wont print
fun(10,10)
print('---------------------------------------')

a,b,c,d=10,11,12,13

def fun3(p=40,q=23):
    x,y,z,w=43,24,54,65
    print('Locals()',locals())

fun3()
print('Globals:',globals())