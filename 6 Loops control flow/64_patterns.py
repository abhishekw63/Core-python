#pattern1
for i in range(0,5):        #no need of nested for loop
    print('*' * 5)
print('----------------------------------')
#pattern2
for i in range (0,5):
    print('*' * i)
print('----------------------------------')
#pattern3
for i in range(5,0,-1):
    print('* ' * i)
#pattern4
for i in range(0,6):        #self
    if i>=3:
        for j in range(3,0,-1):
            print('* ' * j)
        break
    else:
        print('* '* i)


