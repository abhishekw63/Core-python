'''
-> python programme -> cursor -> connection -> driver -> sqlite3 -> database storage.

Here's an explanation of each part:

import sqlite3: Import the SQLite module, which provides a simple way to interact with SQLite databases using Python.

conn = sqlite3.connect('univ.db'): Establish a connection to the SQLite database file named 'univ.db'. If the file doesn't exist, it will be created.

cur = conn.cursor(): Create a cursor object (cur) to interact with the database. The cursor is used to execute SQL queries and fetch results.

cur.execute('create table Dept(deptno integer primary key, dname text)'): Execute a SQL query using the cursor. This query creates a table named 'Dept' with two columns: 'deptno' (an integer, primary key) and 'dname' (a text field).

conn.commit(): Commit the changes made to the database. This step is necessary to save the changes permanently.

cur.close(): Close the cursor. This is good practice to free up resources after executing queries.

conn.close(): Close the database connection. This is also good practice to release resources after working with the database.

So, in summary, the code is creating a SQLite database file ('univ.db'), establishing a connection to it, creating a table named 'Dept' with specified columns, committing the changes, and then closing the cursor and the database connection.
'''

import sqlite3

conn=sqlite3.connect('univ.db')

cur=conn.cursor() # use the cursor to execute the query

#cur.execute('create table Dept(deptno integer primary key,dname text)')
#cur.execute('create table Students(roll integer primary key,name text,city text,deptno integer,foreign key(deptno) references Dept(deptno))')

#cur.execute('.tables') wont work he .tables command is specific to the SQLite command-line interface, not the SQLite Python module.
#cur.execute("SELECT name FROM sqlite_master WHERE type='table';") #will show tables
cur.execute('select * from Dept')
tables=cur.fetchall()
print('Tables of univ DB are',tables)

conn.commit()
cur.close()
conn.close()

'''
-Udemy pdf:
DDL stands for Data Definition Language . 
•DDL include ALTER TABLE, CREATE TABLE, DROP TABLE, CREATE DATABASE, and TRUNCATE TABLE. 
• Python accesses the database through a cursor, 
•We will give queries to cursor object and it will pass to connection
• Connection object will connect to the SQLite3
  it will enable multiple users to work on the same databases. It improved security efficient data access.
  
'''