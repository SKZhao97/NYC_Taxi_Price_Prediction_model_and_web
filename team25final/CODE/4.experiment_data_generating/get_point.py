from csv import reader
from datetime import datetime
from sys import argv
import csv

def normalize_time_stamp(x):
    return 1 - ((143 - x) / 143)


def time_zone(h, m):
    return h * 6 + m // 10

# get latitude and longtitude from csv
# the first parameter is the input file
# the second parameter is the output file

filename = argv[1]
path = argv[2]
p = "projection.csv"
# ---------------------------------------------------
raw_data = open(filename, 'rt', encoding='UTF-8')
readers = reader(raw_data, delimiter=',')
data = list(readers)
# ---------------------------------------------------
lmap = open(p, 'rt')
readers2 = reader(lmap, delimiter=',')
mpp = list(readers2)
del mpp[0]
# ---------------------------------------------------
title = data[0]
title.append('time_stamp')
# title.append('weekday')
title.append('month')
# title.append('week_number'）
title.append('start_ll')
title.append('end_ll')
del data[0]
for i in data:  # start from the second row and add the week number
    x = datetime.strptime(i[1], '%H:%M')
    i.append(time_zone(x.hour, x.minute))
    i.append(12)
    pku = i[3]
    den = i[4]
    for ii in mpp:
        if ii[0] == pku:
            i.append(ii[4])
    for ii in mpp:
        if ii[0] == den:
            i.append(ii[4])
            
f = open(path, 'w', newline='')
csv_write = csv.writer(f)
csv_write.writerow(title)
for i in data:
    csv_write.writerow(i)
