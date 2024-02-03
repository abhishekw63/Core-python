dict1=dict()
dict2={}

d3=dict(((1,1),(2,4),(3,9),(4,16),(5,25)))
print(d3)

l1=[100,81,49,36,25,16,9,4]
l2=[10,9,8,7,5,4,3,2]
d4=dict(zip(l1,l2))
print(d4)
d5=dict(zip(l2,l1))
print(d5)

t1=(1,2,3)
t2=(1,8,27)
d6=dict(zip(t1,t2))
print(d6)
