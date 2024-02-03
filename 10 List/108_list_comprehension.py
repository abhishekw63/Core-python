l1=[]
for x in range(0,10):
    l1.append(x)
print(l1)

l2=[ x for x in range(0,10)] # why is this printing 9?
print(l2)

l3=[x**2 for x in range(1,11)] #with sqauare expresssion
print(l3)

l4=[x for x in range(1,20) if x%2==0]
print(l4)

l5=[x for x in (12,24,42,42,554,22,476,785,45) if x%2!=0]
print(l5)

l6=[x.upper() for x in 'python']
print(l6)

l7=[x for x in 'PyThoN' if x.isupper()]
print(l7)

input_data=input('enter names(separated by space):')
l8=input_data.split()
print(l8)

l9=input('enter the name separated by space:').split()
print(l9)