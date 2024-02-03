#addition of two matrices

l1=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
l2=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
l3=[]

for i in range(3):
    s=[]
    for j in range(4):
        r=l1[i][j]+l2[i][j] #we can try substraction/multiplication/division too.
        s.append(r)
    l3.append(s)

print(l3)

