'''
-pragma table_info(dept);
-select * from dept order by dname; / select * from dept order by dname ASC;
-select * from dept order by dname DESC;
-select * from students order by name desc;
-select * from students,dept; # it will multiply first row of students table to dept.So 15 x 4=60 rows.it is called cartesian product.
-select *  from students where students.deptno=dept.deptno; #joining
-select * from students join dept on students.deptno=dept.deptno; #same as above;
-select * from students as s join dept as d on s.deptno=d.deptno; #can be done using where
-select city from students group by city; #cities name would appear with unique names; 
-select count(*),city from students group by city; #cities name with its count. count is aggregate function
-select count(*),city from students group by city having count(*)>=2; #imposing condition upon groupby that is having.
'''
'''
Order by clause: we can display the content increasing as well as decreasing
Join: in a query we are retrieving the data from multiple table then we have to join the table.
Having: shows which are having 2 or more count.

'''