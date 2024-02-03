'''
->diff betn finally and else block:
    else block wont executed when exception is raised whereas finally block will
    executed in every circumstances
->finally block:
    in function ,if clash arises between returninng value and finally block then
    finally block will first execute and then returns value if exist.
    in other cases returns immediately stops the function.
    i.e. finally block will compulsorily executed
    where it is useful?
        -finally block is useful for cleanup proccess
        -i.e. f.close() inside finally block
'''

'''num1=int(input('num1:'))
num2=int(input('num2:'))

try:
    c=num1//num2
except ZeroDivisionError as msg:
    print(msg)
else:
    print('ans:',c)
finally:
    print('finally block')'''

print('- '* 35)

def division(a,b):
    try:
        res=a//b
        return res
    except ZeroDivisionError as msg:
        raise ZeroDivisionError
    finally:
        print('finally block')
    
print(division(10,0)) #look for finnaly block statement.