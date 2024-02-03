l1=[1,2,3,4]
l2=['a','b','c','d']

dict4=dict(enumerate(l1))
print('1:',dict4)
print('2',type(dict4))

for item in enumerate (l2):
    print(item,end=' ')

print('\n')
dict6={x:x**2 for x in l1}
print('3:',dict6)

dict7=dict((x,x**2) for x in l1)
print('4:',dict7)

l3=[5,6,7]
l4=['a','b','c']

for x,y in zip(l3,l4):
    print(x,y)

d8={ x:y for x,y in zip(l3,l4)}
print('5:',d8)

d9=dict((x,y) for x,y in zip(l4,l3))
print('6:',d9)

l5=['zero','one','two','three']
for x,y in enumerate (l5):
    print(x,y)

d10={x:y for x,y in enumerate (l5)}
print('7:',d10)

d11=dict((x,y) for x,y in enumerate (l5))
print('8:',d11)