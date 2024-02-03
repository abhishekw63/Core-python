#displaying data in given format(25 letters):
'''
    product name........price
    chicken pizza.......30000

'''
item=input('enter the item name:')
price=input('enter the price:')

total_length=len(item)+len(price)

dots='-' * (25-total_length)

print(item+dots+price)
print(len(item+dots+price))