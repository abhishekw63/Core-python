#display credit card number
'''
card no: 1234 5678 1234 5678
display: **** **** **** 5678

'''
credit_card_no=input('enter the credit card number:')
print(len(credit_card_no))

display=credit_card_no[15::]

hidden='*' * 4 + ' '
output=hidden * 3 + display
print(output)
print(len(output))