class Employee:
    employee_count=101#class variable  logic

    def __init__(self,name,salary,designation):
        self.name=name
        self.sal=salary
        self.dsgn=designation
        self.emp_id='e'+str(Employee.employee_count) #logic
        Employee.employee_count+=1 #logic
    def show(self):
        show=f'Name:{self.name}\nSalary:{self.sal}\nDesignation:{self.dsgn}\nEmployee ID:{self.emp_id}'
        return show
    def total_emp(cls):
        return cls.employee_count-int(101)#logic
    
e1=Employee('Raja',10200,'leader')
e2=Employee('Raji',10300,'vice leader')
e3=Employee('Raju',10400,'HR leader')
e4=Employee('Rajo',10500,' Finance leader')

print(e3.show())
print(e1.total_emp())