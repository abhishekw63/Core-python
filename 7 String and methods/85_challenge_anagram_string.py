str1=input('enter the sentence1:')
str2=input('enter the sentece2:')

if len(str1)!=len(str2):
    print('it is not anagram')
else:
    for x in str1:
        if x not in str2:   # i was writting for x not in str2. how is this if condition will check repeatedly in str2 for particular character? shouldnt it only check for one character in beginning of str? in c i have to write 2 loops. explain pls
            print('it is not anagram')
            break
    else:
        print('it is anagram')