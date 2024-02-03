#performing transposition of matrix

l1=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
l2=[]

for j in range(4): #not 3
    s=[]
    for i in range(3): # not 4
        r=l1[i][j]
        s.append(r)
    l2.append(s)

print(l2)