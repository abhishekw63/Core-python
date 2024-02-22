input1=[int (x)for x in input('enter the elements of list1:').split()]
input2=[int (x)for x in input('enter the elements of list1:').split()]
l3=[]

for x in input1:
    if x in input2:
        l3.append(x)

print((l3))
     
# {5, 6, 7}  
# l1=list(range(1,11))
# l2=[5,6,7]
# set_l1=set(l1)
# set_l2=set(l2)
# set_final=set_l1.intersection(l2)
# print(set_final)