'''''def division(a,b):
    if b!=0:
        c=a//b
        return c 
    else:
        return -1

c=division(-10,10) #ans should be -1 buy it will show zero division error.
if c==-1:
    print('Zero division erro')
else:
    print('ans',c)'''''

print('- ' *35)

def division(a,b):
    if b!=0:
        c=a//b
        return c 
    else:
        raise ZeroDivisionError #change

try:
    c=division(-10,10) #will print -1
    print('ans',c)
except:
    print('zero division error')