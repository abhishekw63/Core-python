l1=[x for x in range (0,10)]
print(l1)

t1=tuple(x for x in range(0,10))
print(t1)

#t2=(x for x in range(0,10)) error
#print(t2)

t3=(*(x for x in range(0,5)),)
print(t3)

t4=(*(x for x in range(4)),)
print(t4)

t5=tuple(x for x in range(11,50) if x%2==0)
print(t5)

t6=tuple(x for x in 'python')
print(t6)

#t7=tuple(x** for x in range(5,11)) #wont work

t8=tuple(x for x in 'AbHiShEk' if x.islower())
print(t8)

t9=(10,20,30,40,50,60,70,80,90)
print(t9.index(80))
print(t9.count(20))
#print(t9.index(100)) error