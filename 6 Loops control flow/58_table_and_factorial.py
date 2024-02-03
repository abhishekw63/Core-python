#1.displaying multiplication table using for loop
#2.factorial of number

number=int(input('enter the number: '))
count_table=0

for count_table in range(1,11):
    print(number, 'X', count_table,'=',number*count_table)

count_factorial=1
multiplication=1

for count_factorial in range(1,number+1):
    multiplication*=count_factorial

print('factorial of given number is:',multiplication)