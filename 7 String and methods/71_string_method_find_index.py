s = 'hello how are you?' 

# i  0123456789       17

# s.find(substring, start, end)

print(s.find('o'))             # 4 (First occurrence of 'o' at index 4)
print(s.find('?'))             # 17 ('?' found at index 17)
print(s.find('are'))           # 8 (First occurrence of 'are' at index 8)
print(s.find('x'))             # -1 ('x' is not found in the string)
print(s.find('o', 5))          # 7 (First occurrence of 'o' starting from index 5)
print(s.find('o', 5, 7))       # -1 ('o' not found within the specified range)
print(s.find('o', 8, 17))      # 15 (First occurrence of 'o' within the specified range)

# s.rfind(substring, start, end)

print(s.rfind('o'))            # 9 (Last occurrence of 'o' from the right at index 9)
print(s.rfind('o', 0, 15))     # 7 (Last occurrence of 'o' within the specified range)
print(s.rfind('k'))            # -1 ('k' is not found in the string)

# s.index and s.count

# The next two lines will raise ValueError because 'ks' is not found in the string.
# print(s.index('ks'))         
# print(s.find('k'))

print(s.count('me'))           # 2 ('me' appears twice in the string)
print(s.count('o'))            # 3 ('o' appears three times in the string)
print(s.count('how'))          # 1 ('how' appears once in the string)
