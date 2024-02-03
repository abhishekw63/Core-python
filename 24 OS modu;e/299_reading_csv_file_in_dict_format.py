import csv
import pprint
with open('Excel_CSV.csv','r') as f:
    csv_reader=csv.DictReader(f) #it will return an iterable object
    for row in csv_reader: #individual dictionary with key value pair
        print(row)  
    f.close()

f=open('Excel_CSV.csv','r')
f.seek(0)
csv_reader=csv.DictReader(f)
emp_dict=dict()

for dic in csv_reader:
    emp_dict[dic['name']]=dic
print('\n')
pprint.pprint(emp_dict)

print('employee raj',emp_dict['raj'])