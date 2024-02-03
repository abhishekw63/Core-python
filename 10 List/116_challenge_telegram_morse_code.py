
morse_codes=['._' , '_…' , '_._.' , '_..' , '.' , '.._.' , '__.' , '….' , '..' , '.___']

text='ace'
code=[]

for x in text:
   code.append(morse_codes[ord(x)-97])

code=' '.join(code)

print(code)