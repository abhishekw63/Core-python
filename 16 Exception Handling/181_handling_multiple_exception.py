list1=list(range(1,6))

try:
    index=int(input('enter the index:'))
    print(list1[index])

except IndexError as msg:
    print('invalid index,',msg)
except ValueError as msg:
    print('invalid input,',msg)
'''except (IndexError,ValueError) as  msg:
    print(msg)'''

print('programme terminated gracefully')
