import sqlite3

conn=sqlite3.connect('univ.db')
cur=conn.cursor()

#deptno=int(input('enter dept no:'))
#dname=input('enter dept name:')
#cur.execute('insert into Dept values(10,"CSE")') #can give different order by dname and deptno
#cur.execute('insert into Dept values(20,"ECE")')
#cur.execute('insert into Dept values(30,"Civil")')
#cur.execute(f'insert into Dept values({deptno},"{dname}")')

for i in range(12):
    roll=int(input('roll:'))
    name=input('name:')
    city=input('city:')
    deptno=int(input('dept no:'))
    
    cur.execute(f'insert into Students values({roll},"{name}","{city}",{deptno})')
    


conn.commit()   #mandatory in ddl or dml query 
cur.execute('select * from Students')
tables=cur.fetchall()
print(tables)

conn.commit()
cur.close()
conn.close()
