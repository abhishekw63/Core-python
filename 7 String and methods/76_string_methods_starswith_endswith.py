'''
Start and end are in square brackets so it is optional
s.startswith(prefix [,start[,end]])
s.endswith(prefix [,start[,end]])
s.removesuffix(suffix,/)
s.removeprefix(prefix,/)
s.partition(sep)
s.rpartition(sep)
'''

#s.startswith()

s='my name is abhishek.'
print(s.startswith('my'))
print(s.startswith('m'))
print(s.startswith('is'))
print(s.startswith('abhi',11,18))

#s.endswith()

s='my name is raj patel'
print('-',s.endswith('raj'))
print(s.endswith('patel'))
print(s.endswith('is',0,10))

#s.removesuffix()

s='python'
print(s.removesuffix('on'))

s='abhishek loves python'
print(s.removesuffix('thon'))

#s.removeprefix()

s='abhishek loves python'
print(s.removeprefix('abhishe'))

#s.partition(sep)
'''
->it will divide
->it will check and if available then form a tuple
'''
s='rahulraj will become a backend developer'
print(s.partition('hul'))
print(s.partition('x'))

'''
s.rpartition( sep )
• It will perform from the right hand side'''

s='abhishek will become backend developer'
print(s.rpartition('a'))
