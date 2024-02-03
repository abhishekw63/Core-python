def flattenned(l1):
    for e in l1:
        if hasattr(e,'__iter__'): #catch:iter
            yield from flattenned(e) #catch: yield from
        else:
            yield e

l1=[1,2,[3,4,[6,7],5],8,9]
Generator_ob=flattenned(l1)
for i in Generator_ob:
    print(i,end=' ')

'''
In Python, an object is considered iterable 
if it has an __iter__ method that returns an iterator.
An iterator is an object that defines 
how to traverse or loop through the elements of a container. '''

'''
Objects that can be iterated over,
like lists, tuples, and dictionaries, 
have an __iter__ method that returns an iterator. 
So, to check if an object is iterable, 
you should check if it has an __iter__ method, not attribute.
'''


