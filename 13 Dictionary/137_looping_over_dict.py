print(dir(dict))
#get
#keys
#values
#items

d1={101:'production',102:'sales & marketing',103:'account',104:'inventory'}
for x in d1:
    print(x) #by default keys is printed
print('\n')
for x in d1:
    print(x,d1[x])
print('\n')

for x in d1:
    print(x,d1.get(x)) #get method
print('\n')

print(d1[101])
print(d1.get(101))

#print(d1[106]) keyerror
print(d1.get(106)) #none

print(d1.get(108,'Unknown dept')) #No department available so returns unknown values

print('keys:',d1.keys())
print('values:',d1.values())

print('items:',d1.items())

for k in d1.keys():
    print(k)
print('\n')

for v in d1.values():
    print(v)
print('\n')

for item in d1.items():
    print(item,end=' ')
