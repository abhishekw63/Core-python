s1=set((12,3,4))
print(s1)

#https://chat.openai.com/c/5d9c4231-67b2-4b4f-8dc3-789e7331b0f4
#s2 is generator expression. it produces value when requested so it is memory efficient

s2=(x for x in range(1,11))
print(s2) 

for x in s2:
    print(x,end=' ') #this loop will go through generator and iterate over each value

#print(next(s2)) #raised error because you've gone beyond the end of generator, so it'll raise a stopiteration error

s3={x**2 for x in range(11,16)}
for x in s3:
    print(x,end=',') #trailing comma
print('\n')

s4={x**2.5 for x in range(1,6)}
result=', '.join(map(str,s4))
print(f'{result}.')

s5={x for x in range(1,20) if x%2==0}
result=','.join(map(str,s5))
print(result)

string='phillipines' #hashable type
s6={x.upper() for x in string}
for x in s6:
    print(x,end=' ')

print('\n')
string1={'madam','madam'}
s7={ x for x in string1}
for x in s7:
    print(x,end=' ')

print('\n')
s8={x for x in 'rajaja'}
s9=list[s8]
s10=set(s9) #unhashable type set
for x in s8:
    print(x,end=' ')

'''
In Python, you can create a set with elements that are 
themselves immutable or hashable, such as individual numbers, 
strings, or tuples. However, mutable objects like sets, lists, 
or dictionaries are not considered hashable and cannot be elements of sets.'''

#https://chat.openai.com/c/5d9c4231-67b2-4b4f-8dc3-789e7331b0f4



