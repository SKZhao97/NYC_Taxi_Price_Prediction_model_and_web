from csv import reader
from datetime import datetime
from sys import argv
import urllib.request, json
import csv
# arrange the order of data to fit the input format of prediction model
# the first para is input file
# the second para is output file
filename = argv[1]
path = argv[2]

raw_data = open(filename, 'rt', encoding='UTF-8')
readers = reader(raw_data, delimiter=',')
data = list(readers)
del data[0] #delete the title to get data
new_data = []
title = ["start_point", "end_point", "trip_duration", "trip_distance", "time", "pku", "den", "distance_category", "null", "lyft", "taxi", "time_stamp", "weekday", "month"]
for i in data:
    ii = [i[8], i[9], i[10], i[11], i[1], i[3], i[4], i[2], "useless", i[5], "0", i[6], i[0], i[7]]
    new_data.append(ii)

f = open(path, 'w', newline='')
csv_write = csv.writer(f)
csv_write.writerow(title)
for i in new_data:
    csv_write.writerow(i)