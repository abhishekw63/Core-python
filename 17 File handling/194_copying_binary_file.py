file=open('CB1.png','rb') #b stands for binary mode otherwise unicode..errror
data=file.read()
#print(data)
file1=open('CB2.png','wb')

file1.write(data)
file.close()
file1.close()