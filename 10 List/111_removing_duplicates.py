input_list=[int (x) for x in input('enter the list element separated by space:').split()]
list2=[]
for x in input_list:
    if x not in list2:
        list2.append(x)

print('Using a Loop to Preserve Order:',list2)

result1=set(input_list)
print('Using Set Conversion:',result1)

i=0
result2=input_list
while i<len(result2):
    element=result2[i]

    if result2.count(element)>1:
        result2.remove(element)
    else:
        i+=1
print('Using a Loop',result2)



  

    