#print(dir(dict))
'''
clear', 'copy', 'fromkeys', '
get', 'items', 
'keys', 'pop', 'popitem', '
setdefault', 'update', 'values']
'''
d1={10:'raj',102:'abhi',103:'nilesh',104:'yash',105:'gita'}

d2=d1.copy() #create shallow copy
print('copy',d2)
print('id of d1 10',id(d1[10]))
print('id of d2 10',id(d2[10])) 
#it's still referencing the same objects in memory for the values. 

d2={106:'shivam'}
d1.update(d2) #d3=d1.update(d2) wont work
print('update:',d1)

#setdefault: work likes get. if record not found then it will insert a key and its value be none

print('dictionary1:',d1)
print('get',d1.get(103))
print('setdefault',d1.setdefault(103))

print('get',d1.get(110)) #returns none
d1.setdefault(110) # will add 110 key with none value
print(d1)
 
d1.update({111:'ashish',112:'ritesh'})
print(d1)

#fromkeys-insert keys from other sequences. values will be same
l1=[1,2,3,4]
d4={}
print(d4.fromkeys(l1))
print('fromkeys',d4) #fromkeys method doesnt modify 
d5=d4.fromkeys(l1,'fromkeys')
print('fromkeys',d5)

d1.update(d5)
print(d1)

print('\n')
#pop
d1.pop(4)
print('pop',d1) #4 key-value pain has been removed
#d1.pop(90) returns key errord

print('\n')
d1.clear()  #dictionary will be cleared
print('clear',d1)

del d1 #delete dictionary
