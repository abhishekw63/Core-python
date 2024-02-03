#s.ljust(width[,fill])
#s.rjust(width[,fill])
#s.center(width,[,fill])
'''
-> this method are useful for text alignment'''

s='abhishek'

#print(s.ljust(15,'_'))  #abhishek_______
#print(s.ljust(len(s)+10,'<')) #abhishek<<<<<<<<<<

#print(s.rjust(16,'>'))  #>>>>>>>>abhishek

#print(s.center(16,"*"))
#print(s.center(len(s)+8,'-')) #----abhishek----

#string is immutable so it will not modify it will create a new string

#->this is useful for removing the characters from string
#s.strip([chars])   #it will remove leading char
#s.lstrip([chars])   #tailing removes character
#s.rstrip([chars])  #- removes spaces from both the side

s1='........._+++++++abhishek++++++++_........'
print(s1.strip('.'))    #_+++++++abhishek++++++++_
print(s1.lstrip('.'))   #_+++++++abhishek++++++++_........
print(s1.rstrip('.'))   #........._+++++++abhishek++++++++_
print(s1.rstrip('+'))   #why is + not stripping
print(s1.lstrip('._+')) #abhishek++++++++_........
print(s1.rstrip('+.'))  #........._+++++++abhishek++++++++_

#All this methods will return new string they will generate new string after performing the operations

