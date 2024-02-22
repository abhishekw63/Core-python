# # find the sum of given numbers as input.
# # find the sum of positive and negative numbers.
# num=input('enter the number separated by space')
# l1=num.split()
# l1_all=sum(int(item) for item in l1)
# l1_pos=sum(int(item) for item in l1 if int(item)>=0)
# l2_pos=sum(int(item) for item in l1 if int(item)<0)
# print(l1_pos,l2_pos,l1_all)

#counting the number of digits in a number.
#find sum of digits in a number.
#reversing a number.
# check if a number is a palindrome.
# num=1234321
# num_str=str(num)
# num_sum=sum(int(item) for item in num_str)
# num_rev=num_str[::-1]

# if num_str==num_rev:#     print('palidrome')


#3.find maximum numbers from the given numbers
# num=input('enter number separated by space:')
# num_list=num.split()
# num_max=max(num_list)
# print(num_max)

# #4.convert a decimal number to a binary system
# num=int(input('enter number separated by space:'))
# num_bin=bin(num)
# print(num_bin)
# num_dec=int(num_bin,2) #vice versa
# print(num_dec)

# displaying multiplication table using for loop
# num=int(input('enter number:'))
# for item in range(1,11):
#     print(f'{num} x {item} = {num*item}')
    
# factorial of number
#math.factoriL(num) 
# def factorial(n): #by recursive method
#     if n==0:
#         return 1
#     else:
#         return n  * factorial(n-1)

#1.displaying AP 
# a=int(input('first_num:'))
# n=int(input('upro_term:'))
# d=int(input('difference:'))
# progrssion=[a + i*d for i in range(n)] # logic a+i*d
# # 1 + 0x1
# # 1+ 1x1
# # 1 + 2x1
# print(progrssion)

#displaying Fibonacci series
#[0,1,1,2,3,5,8,13]
# n=int(input('upro_term:'))
# fib_series=[0,1]
# for i in range(n-2):
#     next_sum=fib_series[-1]+fib_series[-2]
#     fib_series.append(next_sum)  
# print(fib_series)

#1.display factors of numbers
# num=int(input('enter number:'))
# factor_list=[item for item in range(1,num+1) if num%item==0]
# print(factor_list)

#2.display whether number is prime or not.
# num=int(input('enter number:'))
# prime=[item for item in range(2,num) if num%item==0]
# if len(prime)==0:
#     print('prime')
# else:
#     print('not prime')

#prime numbers between 1 to 100
#logic: number is divisible by only 1 and number itself count=2
# l1=[]
# for n in range(1,101):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1      
#     if count==2:
#         l1.append(n)       
# print(l1)
#----------------------------


# num=23
# for i in range(2,9):
#     if num%i==0:
#         print('not prime')
#         break
# else:
#     print('prime')






