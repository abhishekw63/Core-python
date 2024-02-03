def pascal(n):
    row=[1]                 #0 1
                            #1 0
    for i in range(0,n): 
        print(row)
        temp_row=[0] + row
        row= row+ [0]
        new_row=[x+y for x,y in zip(row,temp_row)]
        row=new_row

def pascal1(n):
    row=[1]
    for i in range(n):
        print(row)
        row=row +[0]
        temp=[0] + row
        new_row=[x+y for x,y in zip(temp,row)]
        row=new_row

#try to design like complete pascal triangle.
pascal(3)
pascal1(3)