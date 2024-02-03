#assigning countires name alphabetically in dictionary

'''countries=dict()

n=int(input("how many name of countries you want to give:"))

for i in range(0,n):
    name=input('enter the country name:')
    if name[0].upper() not in countries:
        countries[name[0].upper()]=[name]
    else:
        countries[name[0].upper()].append(name)
    
print(countries)'''

print('-'*35)

countries=dict()

countries_name=input('enter countries name separated by space:')
names_list=countries_name.split()

for name in names_list:
    if name[0].upper() not in countries.keys(): 
        countries[name[0].upper()]=[name]
    else:
        countries[name[0].upper()].append(name)

'''

for name in names_list:
    initial_letter = name[0].upper()
    if initial_letter not in countries:
        countries[initial_letter] = [name]
    else:
        countries[initial_letter].append(name)'''  
print(countries)