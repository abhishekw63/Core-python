s1={1,2,30,'z','raj','jac;',True,7+9j}
#no duplicates
#no index
#immutable you can modify or remove but cant'replace
print(s1)
#print(s1[0])
print(type(s1)) 

s2=set((1,2,3,4,5,'true',9.3))
print(s2)
s2.discard(3) # remove and pop for list
print(s2)
s2.add('add')
print(s2) #append extend and insert for list
print(dir(list))

t1=list(range(10,21))
t1.insert(0,100)
print(t1)