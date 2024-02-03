input_list=[int (x) for x in input('enter a number separated by list:').split()]
print(input_list)


s1=''
for x in input_list:
    s1+=str(x) #why cant i write 'x' in argument what does difference it make? 

s2=''.join(map(str,input_list))
print(s2)