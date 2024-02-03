count=1 #dont write 0 because count> number

while count<=10:
    number=int(input('enter the number:'))
    print(number)
    count+=1
    if(count>5):
      break
    

else:
    print('all numbers are printed')

print('end of programme')