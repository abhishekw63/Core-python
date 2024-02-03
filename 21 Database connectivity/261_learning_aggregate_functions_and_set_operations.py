'''
->select count(*) from students; #shows total row /select count(roll) from students; same thing
->select count(distinct name) from students; #ajay is two times so ans :14
->select max(roll) from students;
->select min(roll) from students;
->select sum(roll) from students; # sum of rollnos
->select avg(roll) from students;
->select max(roll),city from students group by city; #max from each city
->select count(roll),city from students group by city; # number of count from cities
->select sum(roll),city from students group by city; #sum of roll of each city
->select * from students where city='Kolkata' union select * from students where city='Delhi'; #union operation
    -select * from students where city='Kolkata'; + select * from students where city='Delhi';  # 
    -select * from students where city='Delhi' or city='Kolkata';# alternatively
->select name from students where city='Mumbai' union select roll,name from students where city='Jaipur'; #wont work because they should have same number as well as same type of columns
-> select name from students where city='Mumbai' union select name from students where city='Jaipur'; #showing name
->select name from students where city='Mumbai' union select name from students where city='Delhi'; # ajay is in both cities but will show only one time
->select name from students where city='Mumbai' intersect select name from students where city='Delhi'; #common name among cities that is ajay
->select name from students where city='Mumbai' except select name from students where city='Delhi'; #except common it will take values from rhs
->select name from students where city='Delhi' except select name from students where city='Mumbai'; # ramesh,verma,ajay - ajay :ramesh,verma
->
'''

'''
-Aggregated function are used with select clause and also used by group by clause
    to work on groups if you don’t use group by it’ll work on entire collection.
-Set operations are Union , Intersection , except.
    The rows or columns taken in set operations must be of same type I.e, 
    if one set contains names the other should also contains names only if not well get an error.

'''