#This method will check if it gives the valid name of the variable
#they all return a Boolean value (True or False) 
#s.isidentifer()
s='if'
print(s.isidentifier()) #True

s='1raj'
print(s.isidentifier()) #False

"""All the ASCII letters , other language letters are printable but there are escape characters \n \t \r
are not printable so it will return false"""
#print(s.isprintable)

s='hello'
print(s.isprintable())

s='abhishek\t wagh'
print(s.isprintable())

'''What are decimal ?? Decimal are the numbers between 0 - 9 
It will say of there are decimal present in the string'''
#s.isdecimal()

s='123'
print(s.isdecimal())

s='1.25'
print(s.isdecimal())

s='12\u00B2'
print(s)
print(s.isdecimal())

'''If you have special numbers it will return true '''
#s.isdigit()

s='123'
print(s.isdigit())

s='1.23'
print('-',s.isdigit())

s='10\u00b2'
print(s)
print(s.isdigit())

s='10\u00BD'
print(s)
print(s.isdigit())

'''It will return true to any number'''
#s.isnumeric()

s='10\u00BD'
print(s.isnumeric())
