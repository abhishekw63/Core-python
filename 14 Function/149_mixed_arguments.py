def add(a,b,c,d,e,f):
    return a+b+c+d+d+e+f

r=add(4,5,6,7,8,8)
print(r)

def add1(a,b,/,c,d,*,e,f): # forward_slash:before values of slash must be positional args
    return a+b+c+d+d+e+f   # asterisk: values after asteriskmust be keyword args

r1=add1(10,20,30,d=30,f=40,e=50)
print('mixed arguemtns',r1)

def add2(a=0,b=0,/): #its good practice to provide default values.
    return a+b

print('forward slash:',add2(1,2)) #must be positional
#function will return None by default.

