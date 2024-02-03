#abs()  underroot a**2 + b**2
print('abs:', abs(-32))
print('abs:', abs(3 + 4j))  # Complex value
print('-'*35)
# Use the ascii() function for explanation
'''
#ascii()
 It returns a string with non-ASCII characters 
 (characters outside the 7-bit ASCII range) escaped using Unicode escape sequences. 
 For example, non-ASCII characters like accented letters or 
 special characters are represented as \\u followed by their Unicode code point.
'''
print('ascii',ascii("A"))
print('ascii',ascii(10))
text = "Café"
ascii_text = ascii(text)

print('ascii',text)
print('ascii',ascii_text)
print('-'*35)

#bin() returns an binary representation of an integer
#bool()
print('bin',bin(4))
print('bin',bin(10))
print('-'*35)

#bool()Returns True when the argument x is true, False otherwise. 
print('bool',bool(10))
print('bool',bool(0))
print('bool',bool(''))
print('bool',bool([]))

#bytearray() and bytes() : used to represent sequences of bytes. 
#bytes: immutable sequence
#bytearray: mutable sequence  
print('bytearray',bytearray(3))
print('byte',bytes(5))

data='hello'
x=bytearray(data.encode())
print('bytearray',x)
for i in x:
    print(i)

x.append(102)
print('Bytearray',x)
print('-'*35)

#callable() returns whether an object is callable

s1='abcde'
n=10
def add(a=0,b=0):
    return 10+2

print('callable',callable(n))
print('callable',callable(s1))
print('callable',callable(add))
print('-'*35)

#chr() returns unicode string of one character.
#ord() Return the Unicode code point for a one-character string.

print('chr',chr(65))
print('chr',chr(97))
print('ord',ord('A'))
print('ord',ord('a'))
print('ord',ord('\u2605'))
print('-'*35)

#dict() used for creating for dictionary
print('dictionary',dict())
print('-'*35)
from pprint import pprint
#dir(): provide details of particular class
print('dir',dir(str))
print('dir',dir(bool))
print('-'*35)

#divmod(): returns tuple (x//y,x%y)

print('divmod',divmod(10,5))
x,y=divmod(11,3)
print('x and y:',x,y)
print('divmod',divmod(15.44,3.4))

print('-'*35)
#enumerate() gives indexing for all items in given sequence

l1=list(range(10,15))
l2=list((3,4,5))
print('Enumerate object:',enumerate(l2))
for i in enumerate(l1):
    print(i,end=' ')
print('-'*35)

#eval() evaluate an expression
print('eval',eval('3*10 / (2+1)'))
print('-'*35)

#exec() executes the python statements
str1='x=10\ny=20\nprint(x+y)'
print('eval',exec(str1))
print('-'*35)

'''
-filter()
-float()
-format()
-frozenset()
-globals()
-hasattr()
-hash()
-help()
-hex()
-id()
-input()
-int()
-isinstance()
-issubclass()
-iter()
'''
#filter()- filter any object from any sequence based on function you give

l1=[3,5,64,4,6,34,65,75,32,45,12,90]

fil1=filter(lambda x:x>25,l1)
print('filter object',fil1)
print('filter',next(fil1)) #can also be done using for loop
print('-'*35)

#float() convert into floating value
str1='90.34253'
print('float',float(str1))
print('-'*35)

#format(): used for formatting and presenting strings in a specified way.
num1=3453464.45
print('format',format(num1,'E'))
formatted_string = "My name is {name} and I am {age} years old.".format(name="Bob", age=25)
print('format:',formatted_string)
print('-'*35)

#frozenset() - set is mutable but this will make it immutable set.
x=frozenset([1,2,3,4,5,5,4,3,2,1])  
print('frozenset:',x)
print('frozenset:',type(x))
print('-'*35)

#globals():Return the dictionary containing the current scope's global variables.
print('globals:',globals())
print('-'*35)

#hasattr: return whether the object has an attribute with the given name.
#-> verifying if you have so and so attribute or not

s1='abcde'
print('hasattr:',hasattr(s1,'lower'))
print('hasattr:',hasattr(s1,'isdigit'))
print('-'*35)

#hash : returns the hash value of object
s1='abcde'
print('hash:',hash(s1))
print('hash:',hash(100))
print('-'*35)

#help : gives details about any method or class
#print('help:',help(iter))
s1='23432'
#print('help:',help(s1.islower()))
print('-'*35)
#hex : base conversion (16)
print('hex:',hex(15))
print('-'*35)

#isinstance:Return whether an object is an instance of class or subclass
#issubclass:return whether class is subclass or not
s1='abcde'
print('isinstance:',isinstance(s1,str))
n1=232.32
print('isinstance:',isinstance(n1,str))

class animal:
    pass
class dog(animal):
    pass

print('issubclass',issubclass(dog,animal))
print('-'*35)
#len(): find length of any object
#list(): create a items of list
'''
locals(): give local variable of function
object(): base class for all python objects
oct() : base conversion function
open(): opening a file
ord() : gives unicode
print(): prints the result
range():gives value in specific range
set(): create object of set class
str():create a object of str class
super(): refers object of super class
tuple(): create a object of tuple class
type(): gives datatype 
'''
#map(): map element of one sequence into another
l1=[1,23,4,4,23,3]
m=map(lambda x:x%1==0,l1)
print('map',m)
print('map',next(m))
print('mapped list:',list(m))
m=map(lambda x:x**2,l1)
print('map',next(m))
print('mapped list:',list(m))
print('-'*35)
#max():gives maximum value in sequence
#min():gives minimum value in sequence
#sum():gives summation of elements in sequence
#sorted(): sort a sequence
#slice():gives slice object of a sequence

l1=[1,2,3,4,5,6]
s=slice(0,4,2)
print('slice object:',l1[s])
print('-'*35)
#zip(): join elements from two sequence

l1=[1,2,3,4,5]
l2=['a','d','e','f','g','c','w','v']
z=zip(l1,l2)
print('zip class:',zip)
print('zipped tuple:',next(z))
print('zipped tuple:',next(z)) 
print('-'*35)
#reversed(): returns a reverse iterator
l1=[1,2,3,4,5,6]
print('reversed iterator object:',reversed(l1))
rev=reversed(l1)
print('reversed element:',next(rev))
print('reversed element:',next(rev))
print('-'*35)
#pow: power of values
#round :round of values
print('power',pow(2,4))
print('round',round(11.33))
print('round',round(12.51))


