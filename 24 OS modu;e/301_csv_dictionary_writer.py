'''
->csv.dictwriter(f,fields)
->writerow()
->writeheader()
'''
import csv
dict1=[{'id':101,'name':'abhi','salary':23443},
        {'id':102,'name':'raj','salary':6344},
        {'id':103,'name':'shivam','salary':6544},
        {'id':104,'name':'rohan','salary':20344}]

fields=['id','name','salary']
with open('excel_csv_dict.csv','w',newline='') as f:
    csv_writer=csv.DictWriter(f,fields)
    csv_writer.writeheader()#if you dont write this then header wont print, directly data will be shown. header will be taken from fields

    for d in dict1:
        csv_writer.writerow(d)
