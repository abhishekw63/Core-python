import sqlite3
conn=sqlite3.Connection('univ.db')
cur=conn.cursor()
'''
->update Dept set dname="Chem" where dname="Mech"
->update Students set city="Bhopal" where roll=15
->delete from Students where roll=15
->delete from Dept where deptno=40
    #referential integrity is we used. 
    # deptno is acting as foreign key for Students table. 
    # 40 will become invalid in students table
    #if properly implemented referential integrity it will cause eroor 

'''
cur.execute('delete from Students where roll=15')

table=cur.execute('select * from Students')
for t in table:
    print(t[0],t[1],t[2],t[3])
    
conn.commit()
cur.close()
conn.close()
