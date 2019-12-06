from csv import reader
from datetime import datetime
from sys import argv
import urllib.request, json
import csv

# add price to each row on column 10
# the first para is the original csv which does not include the fare
# the second para is the new csv file which only contain the price value 
# the third para is the new csv file which contain both trip data and the value
filename = argv[1]
price_path = argv[2]
path = argv[3]
data = list(reader(open(filename, 'rt', encoding='UTF-8'), delimiter=','))
price = list(reader(open(price_path, 'rt', encoding='UTF-8'), delimiter=','))
title = data[0]
del data[0]
x = 0   # index of price
for i in data:
    i[10] = round(float(price[x][0]),2)
    x += 1


f = open(path, 'w', newline='')
csv_write = csv.writer(f)
csv_write.writerow(title)
for i in data:
    csv_write.writerow(i)


