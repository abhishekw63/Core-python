l1=[10,20,['a','b',['c','d'],30,40]]
print(l1)
print(l1[2][2])

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[9,8,7],[6,5,4],[3,2,1]]

c=[]

for i in range(len(a)):
    s=[]
    for j in range(len(a[0])):
        s.append(a[i][j]+b[i][j])
    
    c.append(s)
print('Matrix C:',c)

m=[[4,6,8],[5,8,4],[2,6,0]]
n=[[3,5,3],[6,2,7],[4,3,6]]

sum=[]

for i in range(len(m)):
    s=[]
    for j in range(len(m[0])):
       s.append(m[i][j]+n[i][j])
    
    sum.append(s)

print(sum)

