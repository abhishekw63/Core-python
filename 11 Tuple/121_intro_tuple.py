t1=('jack',90,True,6+9j,45.9,'jack')
print(t1)
print(t1.count('jack'))
print(t1.index(90))
print(t1[4])

t2=((10))
print(type(t2))
print(t2)
t3=(10,)
print(type(t3))
print(t3)

t4=tuple((10,20,30))
print(t4)

t5=()
print(type (t5))

t6=10,20,30,40
print(type(t6))
print(t6)

t7=(11,12,13,14)
a,b,c,d=t7

print(a,b,c,d)
 
l1=[9,8,7,6]
a,b,c,d=l1
print(d)

t8=[22,33,44,55,66,77,88,99]
a,b,c,*d=t8
print(c)
print('-',d)

t9=[7,17,27,37,47]
a,b,*c,d=t9
print(c)

t10=tuple('abhishek')