l1=['pizza','hotdog','nuggets','noodles','burger','french fries']

input_data=input('enter the character:')

for x in l1:
    if x[0]==input_data: #better method: if x.startswith(input_data).
        print('found:',x)
    else:
        pass
    
#try this
# l1=['pizza','hotdog','nuggets','noodles','burger','french fries']

# char=input('enter the char:')

# ans=[item for item in l1 if item[0].startswith(char)]
# print(ans)