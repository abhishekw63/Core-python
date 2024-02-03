list1=[1,2,3,4,5,6,7,8,9]
print('1)',list1[6])
print('2)',list1[-3])

list1[-3]=77
#print(list1)

print('3)',list1[::])

print('4)',list1[3::])
print('5)',list1[3:8])
print('6)',list1[0:10:2])
print('7)',list1[10:-1:-1])

print('8)',list1[::-1])
print('9)',list1[-1:-10:-1])
print('10)',list1[-1:-10:-3])

list1[0:3]=[11,22,33]
print('11)',list1)

list1[0:3]=[111,222]
print('12)',list1)

list1[0:2]=[1111,2222,3333,4444]
print(list1)

list1[0:10]=[1,2,3,4,5,6,7,8,9]
list1[::2]=[11,43,66,88,10]
print(list1)


