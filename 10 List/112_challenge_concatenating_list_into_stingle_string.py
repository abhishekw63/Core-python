input_list=[int (x) for x in input('enter a number separated by list:').split()]
print(input_list)

s1=''
for x in input_list:
    s1+=str(x) #why cant i write 'x' in argument what does difference it make? 

s2=''.join(map(str,input_list))
print(s2)
# -----------------------------------
#this is better 
# [10, 20, 30]
# ['10', '20', '30']
# 102030
# input_list=[int(item) for item in input('num').split()]
# print(input_list)

# str_list=list(map(str,input_list))

# print(str_list)

# ans=''.join(str_list)
# print(ans)

# --------------------------------
# num:12 13 15 16
# ['12', '13', '15', '16']
# [12, 13, 15, 16]
# 12131516

# input_list=[item for item in input('num:').split()]
# print(input_list)

# input_list_int=list(map(int,input_list))
# print(input_list_int)

# final_str=''.join(input_list)
# print(final_str)