from csv import reader
from datetime import datetime
from sys import argv
import csv


# 1. return the time zone，0~6*24-1
# 2. return weekday feature 1~7
# 3. return month feature 1~12
# 4. return the week number 1~52
# the first parameter is input file
# the second paremeter is output file

def normalize_time_stamp(x):
    return 1 - ((143 - x) / 143)


def time_zone(h, m):
    return h * 6 + m // 10


filename = argv[1]
path = argv[2]
raw_data = open(filename, 'rt', encoding='UTF-8')
readers = reader(raw_data, delimiter=',')
data = list(readers)
title = data[0]
title.append('time_stamp')
title.append('weekday')
title.append('month')
# title.append('week_number'）
del data[0]
for i in data:  # start from the second row and add the week number
    x = datetime.strptime(i[0], '%Y-%m-%d %H:%M:%S')
    # 1. return time zone
    i.append(time_zone(x.hour, x.minute))
    # 2. return weekday
    i.append(x.weekday() + 1)
    # 3. return month
    i.append(x.month)
    # 4. return week number
    # i.append(x.isocalendar()[1])
f = open(path, 'w', newline='')
csv_write = csv.writer(f)
csv_write.writerow(title)
for i in data:
    csv_write.writerow(i)
