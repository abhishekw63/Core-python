'''
-> for..else. concept
    if for loop is successfully executed then else block will executed. 
    it is working as confirmation.
-> while...else
    same as above
->try...except..else
    else block will here confirm that there is no exception raised.
    else block wont executed if except block comes to play
    inside try block write only those statementd which may raise exceptions
    better avoid those statements which doesnt cause any exception
    write those inside else block

'''
print('before try block')
a=int(input('num1:'))
b=int(input('num2:'))

try:
    c=a//b
    #print('end of try block')
except ZeroDivisionError as msg:
    print('division by zero is not possible,',msg)
else:
    print('result:',c)

#print('outside try-except-else block.')