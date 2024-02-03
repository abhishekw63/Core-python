'''
-SQL also known as Data Retrieval Language ( DRL ).
-The clauses used for writing queries and retrieval of data are select , from , join , where ,order by , group by , having. 
-Select:
    • Select is used for filtering Columns.
    • Along with select we must use from also without from we cannot create a query. 
    • It is used for specifying the columns of a relation that we want to retrieve.
-from:
    • It is used for specifying a relation name 
    • For instance, from the given data we want student Database then we use the following query.
    - If we want to retrieve all the columns we write * in query.
    -Select distinct deptno from student. 
        If you are using multiple column then distinct will treat 2 rows as duplicate only if all the values are same and not just one common value .
-where:
    • It is used for specifying conditions upon one or more fields / columns 
    • Basically it is used for filtering rows 
    • We can specify the condition in where clause using < , < = , > , > = , = , < , >
    • If you have multiple conditions you can combine them with AND , OR , NOT, LIKE , between__and__ , IN , NOT IN.
    -select * from students where city<>'Delhi'; #other than delhi
    -select * from students where deptno>30; #greater than 30
    -select * from students where deptno>=30 and city='Lucknow';
    -select * from students where deptno>=30 and not (city='Lucknow');
    -select * from students where name like 'A%'; #begin from A
    -select * from students where name like '%y'; #ending must be y
    -select * from students where name like '%m%'; # m must be there between
    -select * from students where deptno between 10 and 30;#getting a range
    -select * from students where roll between 10 and 15;
    -select * from students where city in('Delhi','Jaipur'); / select * from students where city='Delhi' or city='Jaipur';
    -select * from students where city not in('Delhi','Jaipur');
    -
'''