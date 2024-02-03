l1=input('enter the alphabets:').split()

l2=[]


for x in l1:
    if x not in l2:
        l2.append(x)
        temp=l1.count(x)
        l2.append(temp)

print(l2)