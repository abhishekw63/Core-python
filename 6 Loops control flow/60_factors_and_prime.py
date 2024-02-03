#1.display factors of numbers
#2.display whether number is prime or not.

number_factor=int(input('enter the number: '))

for i in range(1,number_factor+1):
    if number_factor%i==0:
        print(i)

print('--------------------------------------')


number_prime=int(input('enter the number:'))
count_prime=0
for i in range (1,number_prime+1):
    if(number_prime%i==0):
        count_prime+=1

if count_prime==2:
    print('number is prime')
else:
    print('number is not prime')
        
