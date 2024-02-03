def net_salary(basic,allowance,deduction):
    net=basic+allowance-deduction
    return net
print('Positional arguments:',net_salary(10,5,2))
print('keyword arguments:',net_salary(10,allowance=5,deduction=2))