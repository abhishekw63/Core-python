working_hours=[int (x) for x in input("enter a working hours oof 6 days separated by space:").split()]
total_hours=sum(working_hours)

wages=int(input('enter the wagesper hour:'))

total_salary=total_hours*wages
print(total_salary)