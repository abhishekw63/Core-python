#default should be on right side.
#keyword shoul be on right side. that is positional argument must not be followed by keyword arg
#default are created only once.

def addItem(item,l1=[]): #(l1=[],item) not possible
    l1.append(item)
    print('inside function:l1',id(l1))
    return l1

print(addItem(22))

l2=[1,2,3,4,5]
print(addItem(6,l2)) #overwrite
print('outside function l2:',id(l2)) #Referring to same object.

print(addItem(33)) #default is appended with 22 before 

