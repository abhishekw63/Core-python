def case_counting(sentence):
    lower_case=[char for char in sentence if char.islower()]
    upper_case=[item for item in sentence if item.isupper()]
    return len(lower_case), len(upper_case)

def case_counting1(sentence):
    lower_count=0
    upper_count=0
    
    for char in sentence:
        if char.islower():
            lower_count+=1
        elif char.isupper(): #include elif because of special characters
            upper_count+=1
        else:
            pass
    return (lower_count),(upper_count) #returns in form of tuple

sentence='AbhIshEk'
lower,upper=case_counting(sentence)
print("Lowercase count:", lower)
print("Uppercase count:", upper)

print(case_counting1(sentence))