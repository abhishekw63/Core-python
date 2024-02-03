#1.counting the number of digits in a number
#2.find sum of digits in a number
#3.reversing a number
#4.check if a number is a palindrome

num_input=int(input('enter the number:'))
count=0
sum=0
rev=0
palindrome=num_input
#remove last digit and form new digit by adding one after after till original number become zero.
while num_input>0:
    mod=num_input%10
    sum=sum+mod
    num_input=num_input//10
    count+=1
    rev=rev*10+mod

print('count is ',count)
print('sum is ',sum)
print('reversed number is ',rev)

if palindrome==rev:
    print('it is palindrome')
else:
    print('it is not palindrome')




