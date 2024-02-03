l1=list(range(1,6))

iterator_object=iter(l1) #converts the list into an iterator
print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))

for i in iterator_object: #will preserve its state
    print('->',i)

#going beyond iterator will raise stopiteration error

#generators:

def days():
    l=['sun','mon','tue','wed','thur','fri','sat']
    i=0
    
    while True:
        x=l[i]
        i=(i+1) % 7
        yield x
    
genrator_object=days() 
print(next(genrator_object))
print(next(genrator_object))
'''
->
When you use yield inside a function, it becomes a generator.
The function returns a generator object, and its state is 
preserved between function calls. Each time you iterate over the generator, 
the function's execution is paused and resumed, and 
it continues from where it left off, producing values one at a time. 
This is useful for creating sequences of values without having to store them in memory all at once. 
Generators are memory-efficient and can be iterated lazily.
'''

'''
->When you use return inside a function, 
it's a regular function that returns a single value. 
Once the return statement is encountered, the function's execution terminates,
and the function returns the specified value. 
Any subsequent calls to the function will start from the beginning,
and it won't remember its previous state.
'''