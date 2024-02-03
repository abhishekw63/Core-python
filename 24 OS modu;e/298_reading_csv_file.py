'''
->comma separated values
->only texts form data not image,audio
->supported by many apps like excel openoffice.automatically form table
->opening excel supported .csv files in notepad shows data separated by comma.
->
'''
import csv
f=open('Excel_CSv.csv','r')

csv_reader=csv.reader(f) #it will return csv object so traverse thorugh it
print(csv_reader)
'''for row in csv_reader: #return in string form
    print(row)'''
print('-----------------------------------------------')
#max salary
next(csv_reader)# need to skip first row as it doesnt encompasses integers
salary=[int(row[2]) for row in csv_reader]
print(salary)
print('max salary',max(salary))
print('-----------------------------------------------')
#max user
f.seek(0) #Seek back to the beginning of the file for another iteration)
next(csv_reader)
max_user=[row[1] for row in csv_reader if (int(row[2]))==max(salary)]
print('maximum salaried person:',max_user)

f.clos()
