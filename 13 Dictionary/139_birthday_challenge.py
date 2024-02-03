d1={
    'sachin':'01/03/1993',
    'abhishek':'02/03/1998',
    'ashish':'20/10/1997',
    'raj':'08/02/1996'
}
name=input('Enter the name of person:')
#print(d1.get(name))

if name in d1.keys():
    print(f'Mr/Miss {name}, your birthdate is {d1[name]}.')
else:
    print('name is not found')
