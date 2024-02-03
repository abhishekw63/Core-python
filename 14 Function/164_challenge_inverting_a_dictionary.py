def invert(dict1):
    d2=dict()
    d2={value:key for key,value in dict1.items()}
    '''for key,value in dict1.items():
        d2[value]=key'''
    return d2

dict1={
    'a':10,
    'b':20,
    'c':30,
    'd':40,
    'e':50,
    'f':60
}
print(dict1)
print(invert(dict1))