'''
Collections:
->clear
->copy
->get
->items
->keys
->values
->update
->most_common
->pop
->pop_item

'''
from collections import Counter
l1=['raj','abhi','shivam','raj','shivam','abhi','rohan','ashish']

c=Counter(l1)
print(1,c)

print(2,c['abhi']) #both give same result
print(3,c.get('abhi'))

print(4,c.keys()) #keys
print(5,c.values())#values

c.update({'bhavik':5})
print(6,c)

print(7,c.items()) #in tuple form
print(8,c.elements()) #returns an object
print(9,':')
for i in c.elements(): #print all element in repeated manner
    print(i,end=' ')

print('\n')
print(10,c.pop('bhavik')) #removed and returns number
print(11,c) #bhvaik will be removed

print(12,c.popitem()) #delete recently added Or Most occuring
print(13,c)

c.update({'nilesh':10})
c.update({'gopal':4})
print(14,c.most_common(3)) #returns three most common elements

c1=c.copy()
print(15,c1) #returns a shallow copy

c1.clear()
print(16,c1) #clear the all elements
