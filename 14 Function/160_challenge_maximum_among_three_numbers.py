def maximum(a,b,c):
    l1=[]
    l1.extend([a,b,c])
    return max(l1) 
    #or return max(a,b,c)

print(maximum(100,10,10))

'''sir's logic
if a>b and a>c:
    return a
elif b>c:
    return b
else:
    return c'''

