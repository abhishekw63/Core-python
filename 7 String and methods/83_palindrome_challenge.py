'''
1.checking a string is a palindrome
2.convert a given string to palindome
'''

str1=input('enter the sentence:')
rev=str1[::-1]

if str1==rev:
    print('it is palindrome')
else:
    print('it is not palindrome')
    print('palindromed sentenced is:'+rev)