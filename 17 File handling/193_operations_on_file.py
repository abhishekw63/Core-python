'''Syntaxes:
->file.read(size)
->file.readline(size)
->file.readlines([sizehint])

->file.write(str)
->file.writelines(sequence)

->file.flush()
    In file handling, the flush() method 
    is used to ensure that 
    the data written to a file is physically stored on the disk.
    i.e. tap example, teacher student catch up speed example.
->file.close()
->readable()
->writable()
->file.tell()
->file.seek(offset[,whence])



'''




'''file=open('prop.txt','w') #same for r also
print(type(file))
print(dir(file))
file.close()
'''
'''file=open('prop.txt','wb') #file object
print(type(file))
print(dir(file))
file.close()'''

'''file=open('prop.txt')
file.close()

#-> this three are the properties of the file
print(file.name)
print(file.mode)
print(file.closed)'''

'''file=open('prop.txt','w')
file.write('this is line1.\n')
file.write('This is line2.\n')
file.write('This is line3.\n')
file.write('This is line4.')
file.close()'''

'''file=open('prop.txt')
    #print(file.read(10)) #single string and type is string
    #print(file.read(20))

    #print(file.readline()) #line 1 #read line by line
    #print(file.readline()) #line 2
    #print(file.readline(6))# file pointer at 7th word of 3rd line.

    #lines=file.readlines() 
    #print(lines,type(lines)) #in the list form
    #lines=file.readlines()
    #for line in lines:#use loop to read line. no need of split method
    #    print(line,end='')
    #-------reading purpose methods over-------#
file.close()'''

'''file=open('prop.txt','w')
    #str1='hello this is abhishek.\nhe learns python gracefully.\nhe aims to be a coder.'
    #file.write(str1)

    #str1=['hellp abhishek.\n','he aims to be a coder.\n','good luck for future']
    #file.writelines(str1)
    #-------writting purpose methods over-------#
file.close()'''


