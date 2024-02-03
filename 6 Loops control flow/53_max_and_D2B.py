#3.find maximum numbers from the given numbers
#4.convert a decimal number to a binary system

size=int(input('how many number would you enter? -> '))
max=int(input('enter number->'))
count=0

while count < size-1:
    number=int(input('enter number->'))

    if(max<number):
        max=number
    count+=1

print('________________________')
print('maximum number is->',max)


#4-> zero will be ignored so this is refined method by converting into string

decimal_number=int(input('enter the number ->'))
binary_number=''

while decimal_number>0:     #try !=0
    mod=decimal_number%2
    decimal_number=decimal_number//2
    binary_number= str(mod) + binary_number

print('binary number is ',binary_number)


