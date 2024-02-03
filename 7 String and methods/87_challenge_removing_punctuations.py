punctuation=''' !@#$%^&*()_+[] {}. ;:"''<>,?/'''
str1=input('enter the sentence1:')
result=''


for x in str1:
    if x not in punctuation:
        result+=x
    else:
        pass

print(result)
