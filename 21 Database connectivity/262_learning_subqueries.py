'''
->select * from students where city in(select city from students where name='Ajay'); 
    subquery will execute and display city in (Mumbai,Delhi)
    it will show all details of students who live in mumbai or delhi
->select * from students where city in (select city from students where name='Ali'); 
    it will show all details of students who live in same city as ALi
->select * from students where deptno= (select deptno from students where name='Ajay');
    show all details of students who has same deptno as ajay
->select * from students where roll > (select roll from students where name='Suraj');
    show all details of studednts who has roll no greater than suraj
-> select * from students where roll > (select avg(roll) from students); 
    show all details of students who has roll no greater than average(8)
->insert into dept values(60,'EEE');
    inserting row in dept table
->delete from dept where dname='EEE';
    whatever row satisfy this condition will be deleted
->update dept set dname='Aero' where deptno=50;
    update the data of dname to Aero row where deptno is 50 
->
'''

'''

'''