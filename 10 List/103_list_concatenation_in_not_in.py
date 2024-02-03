list1=list((5,6,7,8,8))
list2=list1 +[100]

print(list2)
list3=list1.extend([10]) #extend method doesnt return new list it alters original one so try print list1
print('-',list2)

list4=list2 +[11,12,13]
print(list4)

list5=[1,2,3]
print(list5 *3)
#print(list5 *1.5)

print(2 in list5)
print(44 not in list5)