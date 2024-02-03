"""
s.replace(old,new[,count])
s.join(iterable)
s.split([sep[,max split]])
s.rsplit([sep [,max split]])
s.splitlines([keepends])

"""

#s.replace('old','new')

s='my_name_is_abhishek_wagh'
print(s.replace('_','-'))
print(s.replace('_',' '))
print(s.replace('_',' ',3))
print(s.replace('is','was'))

#s.join(s2)
s1='-'
s2='7969'
print(s1.join(s2)) #calling method of s1 and joining upon s2

s1='<->'
s2='abhishek'
print(s1.join(s2))


#s.split()
s='my name is abhishek'
print(s.split())
print(s.split('a'))
print(s.split('-'))
s='my-name-is-abhishek-wagh'
print(s.split('-',3))

#s.rsplit()
#->The s. Split means splitting is done from right hand side

s='my-name-is-abhishek-wagh-.'
print('-',s.rsplit('-',3))

#s.splitlines()
#->works same as split only

s='my\nname\ris\tabhishek\nwagh'
print(s.splitlines())
print(s.splitlines(keepends=True))
