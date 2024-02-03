def pangram(str1):
    str1=str1.replace(' ','') #removing spaces and we can also apply lower method

    sentence=set(str1) #to remove duplicates
    alphabets={chr(number) for number in range(97,123)} #set comprehension

    if alphabets.issubset(sentence): #if alphabets not in sentence: wont work
        print('it is pangram')
    else:
        print('it is not pangram')

def pangram1(str1):
    phrase=str1.replace(' ','')
    phr=set(phrase)
    alpha={chr(item) for item in range(97,123)}
    return phr >= alpha
    '''
    Subset (<=) and Superset (>=):
    '''

str1='The quick brown fox jumps over the lazy dog'
#Pack my box with five dozen liquor jugs
pangram(str1)
print(pangram1(str1)) 

