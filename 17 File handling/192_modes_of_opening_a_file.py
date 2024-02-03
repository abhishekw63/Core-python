'''
mode    Description
r       To read data from file. possibility of filenotfounderror
w       To write data to file. if file exist then make it blank and overwrite it. not available then create new one
a       To append  data to file
r+      read and write (read has priority here)
w+      write and read (write has priority here)
x       file must not be existing already (difference from write mode) fileexistserror
'''

file=open('Write_mode.txt','w') #use dir to know existance
file.write('Hello Write mode')
file.write('i am learning file handling\n')
file.write('if you dont give \\n then content will be in single line!') #check through dir and type cat write_mode.txt
#print(file.read())  wont work because write mode
file.close()

print('-------------------------')
file=open('Write_mode.txt','a') #append mode
file.write('using append mode in file handling\n')
file.write('append mode will preserve previous data on file \n that is ...single line! ')
file.close()

print('-------------------------')

file=open('Write_mode.txt','r+') 
print(file.read()) #last line is single line!
file.write('now in r+ mode write mode will work as append mode.\n')
print(file.read()) 
file.close()

print('-' * 35)

#file=open("Write_mode.txt",'x') #fileexisterror
'''file=open("demo_file.txt",'x') #new created
file.close()'''

'''file=open('MyData.txt','r+') 
file.write('\nappending a new line.')
content=file.read()
print(content)
file.close()'''
'''
r+ mode
->This mode allows both reading and writing to a file.
->If the file exists, it opens the file for reading and writing. 
    If the file doesn't exist, it raises a FileNotFoundError.
->The file pointer is placed at the beginning of the file.
''' 
file=open('MyData.txt','r+') 
file.write('line 2 at beginning')
#file.write('using w+ mode in file handeling.')
content=file.read()
print(content)
file.close()
'''
w+
->If the file exists, it truncates the file to zero length and opens it for writing and reading.
     If the file doesn't exist, it creates a new file for writing and reading.
->The file pointer is placed at the beginning of the file.
'''

#separate practice file for 192
