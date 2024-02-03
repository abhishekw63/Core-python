'''
functions related to files and directory.
->os.name
->os.getcwd()
->os.chdir()
->os.listdir()
->os.mkdir()
->os.makedirs()
->os.remove()
->os.rmdir()
->os.removedirs()
->os.rename()
'''
import os
print(1,os.name) #returns os name
print(2,os.getcwd()) #get current working directory

print(3,os.chdir('C:\\ESD'))#chage directory. it is working in command prompt
#try giving getcwd() now we are in ESD .list dir will show you contents

print(4,os.listdir()) #returns thee content of directory.

'''os.chdir('D:\Study\BACKEND DEVELOPER\python(udemy)')
print(os.getcwd())
print(os.listdir())'''
#above one is for shifting back to D:\Study\BACKEND DEVELOPER\python(udemy) 

#print(5,os.mkdir('C:\ESD1')) #will create a folder in c: named esd1

#print(6,os.makedirs('C:\G_parent\parent\child')) #create nested directory

#print(7,os.remove('C:\G_parent\parent\child\ggl.png')) #remove file

#print(8,os.rmdir('C:\ESD1')) #folder will be deleted

#print(9,os.removedirs('C:\G_parent\parent\child')) #nested folder will be deleted.folder should be empty

#print(10,os.rename('C:\ESD','C:\ESD1'))# it is current working directory
#print(os.getcwd())


print(11,os.rename('D:\ESD','D:\ESD1')) #change will reflect