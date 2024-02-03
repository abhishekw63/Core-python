#python interpret programmes line by line
#expression is piece of code which produces a value

'''
print("abhishek")

print('O----')
print(' ||||')
print('*' * 10)

price=10        # = is assignment operator
price=4.9
name="abhishek"
isPublished=False #case sensitive dont write true instead of True
print(price)

patient_name='John Smith'
patient_age=20
patient_existing=False;
print(patient_name)
print(patient_age)
print("is he existing patient?") 
print(patient_existing)

name=input('What is your name? ' )
fav_color=input("what is your favourite color "+ name + '?') #concatening this stirng using +
print("Hello " + name + '.'+ 'Your favouritet colour is '+ fav_color )
''' 
'''
birth_year=input('what is your birthyear? ') # you will get string '1982' instead of int 1982 therefore convert it
print(type(birth_year))

age=2023 - int(birth_year)
print(type(age))

print(age) 
'''
'''
weight=input('what is your weight in gram? ')
weightKG=int(weight)/1000
print('ypur weight is: ',weightKG)
'''

'''
course1="python's course for beginners."
course2=' python course for "beginners"'
print(course1 + course2)
'''

"""
message=input(''' 
Believe me abhishek,
one day you'll be skilled programmer 
have faith in yourself!
''')
print(message)
"""
"""
course='python'
another=course[:]
another1=course[0:3]
print(course[0])
print(course[1])
print(course[-1])
print(course[-2])
print(course[0:2]) #py
print(course[1:]) #ython
print(course[:4]) #pyth
print(another) #python
print(another1) #pyt
another3=course[1:-1] #ytho
print(another3)
"""
#formatted string
"""
first_name='john'
last_name='smith'
message=first_name + ' ['+ last_name + '] is a coder'
msg=f'{first_name} [{last_name}] is a coder'
print(message)
print(msg)
"""

#string methods
""""
course='abhishek wagh is coder'
print(len(course))  
                            # when function is belong to some kind of object,we refer to  that fn as method
                            #here upper fn specific to string. in contrast print and len are general puprpose fn, they dont belong to string numbers or any kind of object
print(course.upper()) #this doesnt modify original variable
print(course)   
print(course.lower())   
print(course.find('h'))     #find method is case sensitive
print(course.find('wagh'))    #returns index 
print(course.replace('coder','skilled coder'))
print(course.replace('a','A'))
print('was' in course) #in operator returns boolean value     
"""
""""
#arithmetic operations         
print (10/3)
print(10//3)
print(10%3)
print(10 ** 3 )
x=10
x=x+3  #x+3 augmented assignment operator
print(x)
"""
"""
#operator precedence
x=(10 + 3) * (2  ** 2)
print(x)
"""

"""
#math functions
x=2.9
print(round(x))
print(abs(-2.9))

import math # importing math module. math is an object  so accessing using dot operator
print(math.floor(2.9)) #try math. and look for all other mathematical functions
"""
"""
#if statement
is_hot=False
is_cold=False
if is_hot:
    print('drink plenty of water')

elif is_cold:
    print('wear warm clothes')

else:
    print('enjoy your day')
"""
"""
#tutorial
price_of_house=1000000
is_good_credit=False

if is_good_credit:
     
    down_payment=price_of_house*0.1
else: 
    down_payment=price_of_house*0.2
print(f'Down payment: ${down_payment}')
"""
"""
#logical operator
# and: both conditions should be true
# or: atleast one condition should be true
# not:reverses  
has_good_credit=True
has_high_income=True
has_criminal_record=True

if has_good_credit and has_high_income:
    print('eligible1')
else:
    print('not eligible1')

if has_good_credit and not has_criminal_record:
    print("eligible2")
else:
    print('not eligible2')
"""
"""
#comparison operator
# > < >= <= == !=

temperature=30

if (temperature>30):
    print("it is hot day")
else:
    print("it's not hot day")
"""

"""
#tutorial
user_name=input('enter your good name!:')
size=len(user_name)
if (size<3):
    print("Oops! your name size is too small.")
elif(size>10):
    print("Oops!your name is too long")
else:
    print('Your name looks good!')
"""
"""
#project_weight_converter

weight=int(input("What is your weight? "))
answer=input('is it in KG or Lbs? ')

if(answer== 'KG' or  answer.lower()=='kg'):
    Lbs=(weight)*2.2
    print(f'your weight in pound is: {Lbs}')
else:
    Kg=(weight)/2.2
    print(f'your weight in kg is: {Kg}')
"""
"""
#while loops
i=1
while(i<=5):
    print('*' * i)
    i+=1
print('Done')
"""
"""
#guessing game
secretNumber=9
guessAttempt=3
guessCount=0

while(guessCount<guessAttempt ):
    guess=int(input('enter your number: '))
    guessCount+=1
    if(guess==secretNumber):
        print('You won!')
        break
else:
    print("Better luck next time!")
    print(f'secret number is {secretNumber}')
"""

'''
#car game
command=''
started=False
while(True):
    command=input(">").lower()
    
    if(command=='start'):
        if (started):
            print("car is already started")
        else:
            print('car is started')
            started=True


    elif(command=='stop'):
        if(not started):
            print("car is already stopped")
           
        else:
            started=False
            print("car is stopped")

    elif(command=='quit'):
        print('bye bye')
        break
    elif(command=='help'):
        print("""
              start -> to start the car
              stop -> to stop the car
              quit -> to exit """)
    else:
        print("i don't understand that")

 '''
"""
#for looop
for item in 'abhishek':
    print(item)

for item in ['abhishek','raj','rohan']:
    print(item)

for item in [1,2,3,4]:
    print(item)

for item in range(10): #range(5,10) range(5,10,2)
    print(item)
"""

"""
#tutorial
prices = [10,20,30]
total=0
for price in prices:
    total+=price
print(f'total: {total}')
"""
"""
#nested loops
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
"""
#challenge
"""
numbers=[5,2,5,2,2]
for numberCount in numbers:
    print('*' * numberCount) #easy one


numbers=[5,2,5,2,2]     #printing F
for x_count in numbers:
    output=''
    for count in range(x_count):
        output = output + 'x'

    print(output)

#printing L
numbers=[1,1,1,1,5]

for i in numbers:
    output=''
    for j in range(i):
        output+='X'
    print(output)
"""
"""
#lists
names=['abhishek','raj','rohan','yogi','hardik']
print(names)
print(names[2]) #whenever we use square bracket with colon we get new list
print(names[-2])
print(names[2:])
print(names[2:4])
print(names[:])
names[0]='abhi'
print(names)
"""
"""
#challenge: WAP to find largest number in list
numbers=[2,4,6,6,23,64,21,56,32]
max=numbers[0]
for number in numbers:
    if(max<number):
        max=number

print(max)
"""

"""
#2d lists
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix[0][1]=0
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)
"""

"""
#list methods
numbers=[3,4,6,6,89,43,23]
   # numbers.append(100)
   # print(numbers)
   # numbers.insert(0,1)
   # print(numbers)
   # numbers.remove(6)
   # print(numbers)
   # numbers.clear()
   # print(numbers) 
   #numbers.pop()
   #print(numbers.index(89))
   #print(numbers.index(50))
   #print(50 in numbers)
    #print(numbers.count(6))
    #print(numbers.sort()) #doesnt return any value #numbers.reverse()

    #numbers2=numbers.copy() #changes wont impact another list
    #print(numbers2.append(0))
    #print(numbers2) 
"""

"""
#challenge: wap to remove duplicate numbers from list

numbers=[1,2,3,45,6,6,7,88,88,11]
unique=[]
for iterate in numbers:
    if iterate not in unique:
        unique.append(iterate)
print(unique)
"""

"""
#tuples:similar to list but we cant modify/mutate/change tuples
numbers=(1,2,3)
print(numbers.index(1))
numbers[0]=10
print(numbers[0])
"""
"""
#unpacking:
coordinates=(1,2,3) # this goes true for [] also. i.e coordinates=[1,2,3]
#x=coordinates[0]
#y=coordinates[1]
#z=coordinates[2]

# or we can use this feature of python
x,y,z=coordinates
print(z)
"""
"""
#dictionaries: starts with curly brackets

customer={
    "Name":"abhishek wagh",
    "Age":31,
    "BOD":"21 Jan 1980"
}

#print(customer['Name'])
#print(customer['name'])
#print(customer.get("BOD"))  #same as above 
#print(customer.get("Name"))
#print(customer.get("is_verified",False))    #adds defaults value if not present

customer['Name']='Raj R'
print(customer.get('Name'))

customer['BOD']='1 march 1901'
print(customer['BOD'])   
"""
#challenge: printing phone number

phone_number=input('phone number: ')

dictionary={
    '1':'one', '2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','0':'zero'  
}
output=''

for ch in phone_number:
    output=output + dictionary.get(ch,'!') + ' '

print(output)