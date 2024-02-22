morse_codes=['._' , '_…' , '_._.' , '_..' , '.' , '.._.' , '__.' , '….' , '..' , '.___']

text='ace'
code=[]

for x in text:
   code.append(morse_codes[ord(x)-97])

code=' '.join(code)

print(code)

# m_code=[(ord(item)-97) for item in text]

# for item in m_code:
#     print(morse_codes[item],end='   ')