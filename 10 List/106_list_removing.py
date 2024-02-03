#pop()
#remove(x)
#clear()
 
l1=[5,6,7,8]
print(l1.pop())
print(l1)

print(l1.pop(0))
print(l1)

#print(l1.remove(6))
l1.remove(6)
print(l1)

#print(l1.clear())
l1.clear()
print('-',l1)
print(type(l1))
print(len(l1))

l1=[5,6,7,8]

del l1[3]
print(l1)

del l1[0:2]
print(l1)

l1[:]=[]
print(l1)

l1=[5,6,7,8]
l1.clear()
print(l1)

l1=[5,6,7,8]
del l1[0:3]
print(l1)