'''
->sequential access vs random access:
    random access:accessing the data from file at any byte you can jump on and 
    you can access.
    we can randomly access binary files only.
->if you want to close file automatically then open a file with 'with' statement
->converting string into binary data: 2 method-> b' and encode
->seek method: it will move file pointer by given numbers of byte you want
    seek(offset,from)
->tell:it will tell you where thefile pointer is pointing
'''

'''with open('my.data','wb') as f:
    #f.write(b'abcdefghij')
    f.write('abcdefghi'.encode())  '''  
'''



'''
with open('my.data','rb') as f:
    #print(f.read()) # will get in binary form. use decode
    #print(f.read().decode())
    print(f.read(2)) #pointer will be at c
    #print(f.seek(2,1)) #it will print index 4
    f.seek(2,1) #move 2 byte from current poaition
    print(f.read(1))
    f.seek(5,0) # move 5 byte from beginning that is from index 0
    print(f.read(1)) #will print f
    f.seek(-1,2) #move 1 byte from last index
    print(f.read(1))
    f.seek(-3,1) # move 3 byte from backwards from current position
    print(f.read(1))
    print(f.tell()) # it is at 7th index
    f.seek(-4,1)
    print(f.read(2))   
'''
    a b c d e f g h i j
    0 1 2 3 4 5 6 7 8 9
  -10 9 8 7 6 5 4 3 2 1
'''