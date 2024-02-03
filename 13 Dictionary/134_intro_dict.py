dict1={10:'raj',11:'abhi',12:'gopal',13:'rohan',14:'yash'}
print(dict1)
print(dict1[12])
#print(dict1[1]) # key error
dict1[15]='ashish'
print(dict1)

print(dict1[12])

del dict1[12]
print(dict1)

for i in dict1: #only keys
    print(i)

for i in dict1:
    print(i,dict1[i])
