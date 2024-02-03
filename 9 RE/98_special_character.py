from re import *
#c=match('[a-z]','a').group() #only single character  from a to z
#print(c)

#c=match('[a-z]','ndai').group() #only single character / try 0
#print(c)

#c=match('[^a-z]','AB').group() #only single character  except from lower case a to z
#print(c)

#c=match('[a-z]+','abhishek').group() #anything from a to z with repetation
#print(c)

#c=match('[^A-Z]+','raj').group() #anthing with repetation except upper case A to Z
#print(c)

#c=match('[a-z]+|[A-Z]+','abhiSHEK').group() # try ABHIshek
#print(c)

#c=match('([a-z]+)|([A-Z]+)','AbHiS').group() 
#print(c)

#c=match('[.]+','abhishek123').group() #dont know
#print(c)

#c=match('^hell','hello worldd').group() #starting with try 'he'
#print(c)

#c=match('lo$','hello').group() #dnt knw
#print(c)


x=r'llo$' #raw string
c=compile(x)
r=c.search('hello')
a=r.group()
print(a)

#https://chat.openai.com/c/17fa2b6d-b35f-46d3-8c7c-17f808b80261