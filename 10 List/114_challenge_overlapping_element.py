input1=[int (x)for x in input('enter the elements of list1:').split()]
input2=[int (x)for x in input('enter the elements of list1:').split()]
l3=[]

for x in input1:
    if x in input2:
        l3.append(x)

print((l3))
     