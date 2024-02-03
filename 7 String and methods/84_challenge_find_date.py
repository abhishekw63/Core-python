date=input('enter the date in DD/MM/YY format:')
first_slash=date.find('/')
second_slash=date.rfind('/')

day=date[0:first_slash:]
month=date[first_slash+1:second_slash:]
year=date[second_slash+1::]
print('date:'+day+''+' month:'+''+month+' year:'+''+year)

#using split
list1=date.split('/')
print('day:'+list1[0])
print('month:'+list1[1])
print('year:'+list1[2])
