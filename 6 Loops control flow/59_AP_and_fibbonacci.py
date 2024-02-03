#1.displaying AP 
#2.displaying Fibonacci series


a=int(input('enter the first number:'))
d=int(input('enter the difference:'))
n=int(input('enter the terms you want:'))

for term in range(a,a + n*d,d):   #my logic: n*d +1
    print("Term:",term)

print('---------------------------------------------------------')
number_fibonacci=int(input('how many numbers you want? '))
a1=0
b1=1


for i in range(number_fibonacci):              
  print(a1)                     
  c=a1+b1  
  a1=b1                          
  b1=c      

#a      b       c
# 0     1       1
# 1     1       2
# 1     2       3    
# 2     3       5
# 3     5       8                 
                                
 