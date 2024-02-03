def summation(l1):
    l2=[item for item in l1 if item%10==0]
    return sum(l2)

l1=[100,344,222,900,232,400,534,90]
print(summation(l1))