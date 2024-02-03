str1=input("enter the sentence:")
lower=''
upper=''
for x in str1:
    if x.islower():
        lower+=x
    else:
        upper+=x

sentence=lower+upper
print(sentence)