covid=[('country','doses','people','percentage'),('india','165cr','324cr',61),('indionesia','465cr','344cr',63),('china','165cr','324cr',61)]
import csv
with open('covid.csv','w',newline='') as f: #newline is empty because there will be space between each row
    csv_writer=csv.writer(f)

    for tup in covid:
        csv_writer.writerow(tup)

