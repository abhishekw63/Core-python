#1.find the sum of given numbers as input.
#2.find the sum of positive and negative numbers.

number_count=int(input('how many numbers would you enter? '))
count=0
sum=0

while count<number_count:
    number=int(input('enter the number:'))
    sum=sum+number
    count+=1

print('summation of numbers is:',sum)

print('--------------------------------------------------------------------')

number_count1=int(input('how many numbers would you enter in 2nd programme? '))
count1=0
Psum=0
Nsum=0

while count1<number_count1:
    number1=int(input('enter the number:'))
    if(number1>=0):
        Psum=Psum+number1
    else:
        Nsum=Nsum+number1

    count1+=1

print('summation of numbers in 1st programme is:',sum)
print('summation of +ve and -ve numbers in 2nd programme is ',Psum,'and' ,Nsum)
