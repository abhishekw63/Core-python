#-> wont recommend
#-> can handle by multiple except blocks.
try:
    a=int(input('num1:'))
    try:
        b=int(input('num2:'))
        try:
            c=a//b
            print(c)
        except ZeroDivisionError as msg:
            print(msg)     
    except ValueError as e:
        print('error in num2',e)  
except ValueError as e:
    print('error in  num1,',e)

'''
-> Look previous codes for simplified version.
'''