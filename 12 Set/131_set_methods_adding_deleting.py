dir(set)
'''
add
clear
copy
pop
remove
discard
'''
s1=set(range(1,5))
print(s1)

s1.add(5)
print(s1)
#s1.add(6,8)  typeerror:takes exactly one argument. use update method

s2=s1.copy()
print('s2',s2)

s1.update((6,7)) 
print(s1)
s1.update({8,9})
print(s1)

print('removed from s2:',s2.pop()) #randomely element will be removed
print(s2)
#s2.pop(4) #takes no argument. use discard to specifically remove something
#print(s2)

s2.discard(4)
print('removed 4 from s2:',s2) #only removes one element not multiple
s2.discard(4)
print('already 4 removed:',s2) #if availbe it will delete otherwise ignore

#s2.remove(4) # if available then it will delete it otherwise it will raise an keyerror
#print(s2)

s2.clear()
print('empty set:',s2) 

