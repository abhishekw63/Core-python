import sqlite3
import pprint
conn=sqlite3.connect('univ.db') #c:\ if different path
cur=conn.cursor()
'''
->select * from Students
->select name from Students
->select distinct name from Student
->select * from Students where city="Delhi
->select name from Students where name like "A%"
->select roll, name from Students where not city in("Delhi","Mumbai")
->select Students.roll,Students.name,Dept.dname from Students,Dept where Students.deptno=Dept.deptno
->select count(*),city from Students group by city #roll,name anything work instead of *
->select count(*),city from Students group by city having count(*)>2
->

'''
rows=cur.execute('select name from Students where city in (select city from Students where name="Verma")')
#print(rows.fetchone())
#print(rows.fetchmany(3))
#pprint.pprint(rows.fetchall())
all_rows=rows.fetchall()

#print('Roll  Name   City    Deptno')
for t in all_rows:
    #print(t[0],t[1],t[2],t[3]) # every first,second.third,fourth element of tuple
    #can give string formatting 
    print(t[0])
        
cur.close()
conn.close()