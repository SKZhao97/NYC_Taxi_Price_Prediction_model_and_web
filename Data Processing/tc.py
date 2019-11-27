from csv import reader
from datetime import datetime
from sys import argv
import csv


# 1. 返回一天中的时间段，0~6*24-1
# 2. 返回周几的feature 1~7
# 3. 返回月份的feature 1~12
# 4. 返回周数 1~52
# 第一个参数为输入文件
# 第二个参数为输出文件

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
    x = datetime.strptime(i[0], '%m/%d/%Y %H:%M')
    # 1. 返回一天中的时间段
    i.append(time_zone(x.hour, x.minute))
    # 2. 返回周几
    i.append(x.weekday() + 1)
    # 3. 返回所在月份
    i.append(x.month)
    # 4. 返回所在周
    # i.append(x.isocalendar()[1])
f = open(path, 'w', newline='')
csv_write = csv.writer(f)
csv_write.writerow(title)
for i in data:
    csv_write.writerow(i)
