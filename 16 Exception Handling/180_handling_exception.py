l=[1,2,3,4,5,6,7]

try:
    index=int(input('enter the index:'))
    print(l[index]) #this line would cause exception so further statements wont run
    print('end of try block')
except:
    print('invalid index') #exception raised.

print('programme terminated gracefully')