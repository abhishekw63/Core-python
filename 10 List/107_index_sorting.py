#sort(key=none,reverse=True)
#sorted(iterable, key=None, reverse=False)
#index(x)  index(value,start,stop)
#count(X)
#reverse()


list1=[6,6,4,2,1,4,5,2,2,5,6,7,8,0,9,2,2,4]
print(list1.index(0))
print(list1.index(2))
print('-',list1.index(2,4,len(list1)))
print(len(list1))
print(list1.index(2,8,18))

#print(list1.index(10))
print(list1.count(2))
print(list1.count(1))
print(list1.count(11))

print(list1)
#print(list1.reverse())
list1.reverse()
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

l1=['A','bb','cc','AA','e','a','zz','oo','dd','CC']
l1.sort()
print(l1)
l1.sort(key=str.lower,reverse=True) # makes the sorting case-insensitive.
print(l1)

l2=['A','bb','cc','AA','e','a','zz','oo','dd','CC']
print(l2)
l3=sorted(l2)
print(l3)



