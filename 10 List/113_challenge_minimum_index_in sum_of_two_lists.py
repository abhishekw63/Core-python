input_list1=input('enter a your favourite dishes:').split()
input_list2=input("enter raj's favourite dishes:").split()

i1=10
i2=10

for i in range(0,len(input_list1)):
    index2=input_list1.index(input_list1[i])
    
    if i+index2 < i1+i2:
        i1=i
        i2=index2
    
print(input_list1[i1],i1+i2)

