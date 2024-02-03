'''
->os.path.exists()->whether the path exists or not
->os.path.isfile()
->os.path.isdir()
->os.path.split()
->os.path.join()
->os.path.basename()
->os.path.dirname()
->os.path.getmtime()
->os.path.getatime()
->os.path.getctime()
->os.path.relpath()
->os.path.abspath()
'''
import os
print(1,os.path.exists('C:\\ESD\ggl.png')) #path is valid returns true
print(2,os.path.exists('C:\ESD\ggl1.png'))#path is not valid return false

print(3,os.path.isfile('C:\ESD\ggl.png'))#whether file is regular file
print(4,os.path.isdir('C:\ESD\ggl.png'))#whether dircetory or folder exists?
print(5,os.path.isdir('C:\ESD'))

print(6,os.path.split('C:\ESD\ggl.png')) #splits a pathname and file in tuple
print(7,os.path.split('C:\ESD'))

print(8,os.path.join('C:\ESD','ggl.png'))# opposite of split. i.e. join pathname and file/folder

print(9,os.path.basename('C:\ESD\ggl.png')) #only file name
print(10,os.path.dirname('C:\ESD\ggl.png')) #only dir/fol name

print(11,os.path.getmtime('C:\ESD\ggl.png'))#  It returns a timestamp, the number of seconds since the epoch (January 1, 1970).
import time
print(12,time.ctime(os.path.getmtime('C:\ESD\ggl.png'))) #returns modified time

print(13,os.path.getatime('C:\ESD\ggl.png'))
print(14,time.ctime(os.path.getatime('C:\ESD\ggl.png')))#returns last accessed time

print(15,time.ctime(os.path.getctime('C:\ESD\ggl.png')))#returns time of creation

'Right now i am here:D:\Study\BACKEND DEVELOPER\python(udemy)'

print(16,os.path.relpath('D:\Study\BACKEND DEVELOPER\\tops')) #..\tops. cd.. to back one dir. returns a relative path
print(17,os.path.abspath('..\\tops')) #returns absolute path