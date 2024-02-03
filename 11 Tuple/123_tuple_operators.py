t1=(1,2,3,4,5)

for x in t1:
    print(x,end=' ')

print('\n')
for i in range(0,len(t1)):
    print(t1[i],end=' ')

print('\n')
print(t1[3])

#t1[3]=34

print(t1[::-1])
print(t1[1:3])
print(t1[3::])

for i in range(len(t1)):
    print(t1[i],end= '-')

print('\n')
i=0

while i <len(t1):
    print(t1[i],end=' ')
    i+=1

print('\n')
t1=('raj',45,True,7+9j,9.33)
print(t1[-2])
print(t1[:])
print(t1[2:])
print(t1[-1:-(len(t1)+1):-1])
print(t1[::-1])
print(t1[::2])

t3=(9,8,6)
t4=(3,4,1)
print(t3+t4)
print(t1+(1,2,3))
#t5=tuple(1,2,3)+([12,3,4]) # error
#print(t5)

print(t3*3)
print(6 in t3)
