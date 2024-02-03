'''file=open('demo1.txt','w') #take by default r mode
file.write('i am writing the sentence.\n')
file.write('this is line 2.')
file.close()'''

'''file=open('demo1.txt','r')
content=file.read()
print(content)
file.close()'''


'''file=open('demo1.txt','w') #content overwritten
file.write('where could be file pointer?\n Probably at beginnig\n')
file.close()
'''

'''file=open('demo1.txt','r+')
file.write('this is use of read and write mode\n') #file pointer at beginning
file.close()'''

#to add data at the end first apply read mode so that file pointer assumes last position
#and then go for writting mode.