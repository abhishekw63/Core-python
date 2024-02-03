l1=[5,6,7,8]
print(len(l1))
l1.append(9)
print(l1)
#l1.append(10,11,12)
#print(l1)
l1[4:]=[10]
print(l1)
l1[len(l1):]=[11]
print(l1)
l1[6:6]=[12]
print(l1)

#l1.extend(11,12,14)
l1.extend([13,14,15])
print(l1)

l1.extend('abx')
print(l1)

l1.extend(['xyz','opy'])
print(l1)

print(len(l1))

l1[len(l1):]=['zz']
print(l1)

l1.insert(0,25)
print(l1)

l1.insert(len(l1)-1,'pp')
print(l1)

l2=[5,6,7,8]
l2[0:0]=[25]
print('-',l2)

l3=l2.copy()
print('-',l3)
print(id(l2))
print(id(l3))
print(id(l2[0]))
print(id(l3[0]))