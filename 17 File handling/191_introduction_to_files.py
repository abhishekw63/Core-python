file_handler=open('MyData.txt','r') #file pointer

print(type(file_handler))
print(file_handler)

#print(file_handler.read())
str1=file_handler.read() #exhausted file data so need to open again
print(str1)
file_handler.close() #good practice to release resources
#print(type(str1))
print('----------------------------')

file_handler=open('MyData.txt','r') 
print(file_handler.read(6))
print(file_handler.read(10)) #wont start from beginning. file pointer preserved its position
