a=22
b=7
c=22/7
print('division of {0} and {1} is {2}'.format(a,b,c))
print('division of {} and {} is {}'.format(a,b,c))
print('division of {} and {} is {}'.format(c,b,a))
print('division of {2} and {1} is {0}'.format(c,b,a))

print('\u2794 division of {2} and {1} is {0}'.format(c,b,a))
print('\u2794 division of {0:10} and {1:5} is {2:20}'.format(a,b,c))
print('\u2794 division of {0:<10} and {1:<10} is {2:<20}.'.format(a,b,c))
print('\u2794 division of {0:>10} and {1:^10} is {2:>20}.'.format(a,b,c))

print('\u2794 division of {0:<10} and {1:<10} is {2:2F}.'.format(a,b,c))
print('\u2794 division of {0:<10} and {1:<10} is {2:2E}.'.format(a,b,c))

print(f'\u2794 division of {a:^5} and {b:^5} is {c:^5f}')


