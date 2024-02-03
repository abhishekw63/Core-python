l1=['pizza','hotdog','nuggets','noodles','burger','french fries']

input_data=input('enter the character:')

for x in l1:
    if x[0]==input_data: #better method: if x.startswith(input_data).
        print('found:',x)
    else:
        pass
