from csv import reader
from datetime import datetime
from sys import argv
import urllib.request, json
import csv

# get trip distance and trip duration from google distnce matrix api
# the first para is input file
# the second para is output file
req = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="
key = "&key=your_key"

filename = argv[1]
path = argv[2]
raw_data = open(filename, 'rt', encoding='UTF-8')
readers = reader(raw_data, delimiter=',')
datax = list(readers)
title = datax[0]
title.append("trip_duration")
title.append("trip_distance")
del datax[0]

for i in datax:
    pku = i[8].replace(" ", "")
    den = i[9].replace(" ", "")
    url = req + pku + "&destinations=" + den + key
    response = urllib.request.urlopen(url)
    website = json.loads(response.read())
    i.append((website['rows'][0]['elements'][0]['duration']['value']))
    i.append(website['rows'][0]['elements'][0]['distance']['text'].split()[0])

f = open(path, 'w', newline='')
csv_write = csv.writer(f)
csv_write.writerow(title)
for i in datax:
    csv_write.writerow(i)