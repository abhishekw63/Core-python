'''
->Regular expressions (regex or regexp) are used for pattern matching and text manipulation. 
->They provide a concise and flexible way to search, match, and manipulate strings based on specific patterns.
->In Python, we have to import re module for using Regular Expressions.
'''


from re import *

#c=match('abhishek','abhishe').group() #only abhishek search would work
#print(c)

#c=match('abhi|shek','abhi').group() #only abhi or sheck pr abhi from abhishek would work
#print(c)

#c=match('abhishek','abhisheka').group() #only abhishek.... search would work
#print(c)

#c=match('[abhi]','hbabhi').group() #either a or b or h or i search would work
#print(c)

#c=match('[abhi]+','abaababhiababhihahah').group() #any repeatation search would work
#print((c))

#c=match('[abhi]+','aaaaaaaaa').group() #any repeatation search would work
#print(c)

#c=match('[abhi]+','abaababhiababhihahah').group() #any repeatation search would work
#print(c)

#print(dir(RegexFlag))
#https://chat.openai.com/c/17fa2b6d-b35f-46d3-8c7c-17f808b80261

c=match('[abhi]{2}','hiab').group() #only first two would searched
print(c)

import re

pattern = r"hello"
text = "hello world"

if re.search(pattern, text):
    print("Match found!")
else:
    print("No match found!")






