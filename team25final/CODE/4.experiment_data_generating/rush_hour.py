from csv import reader
from datetime import datetime
from sys import argv
import urllib.request, json
import csv
import random as rd
import time

'''
google may block our request if request too frequently.
In this case, the parameter i in the for loop can be reduced,
and run the rush_hour.py, weekday.py repeatedly. If you need to run them repeatedly,
remember to modify the csv.write mode to 'a',
and delete the write title row to avoid write the title repeatedly in the csv.
'''
# different time experiments
# generating 4 csv file which contains 200 fake trips data
req = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="
key = "&key=your_key"
raw_map = "projection.csv"
filename1 = "early_morning.csv"
filename2 = "morning_rush_hour.csv"
filename3 = "afternoon_rush_hour.csv"
filename4 = "midnight.csv"
# load the project.csv as list
mpp = list(reader(open(raw_map, 'rt'), delimiter=','))
del mpp[0]

title = ["pickup_location","dropoff_location","trip_duration","trip_distance","RatecodeID","PULocationID"
        ,"DOLocationID","fare_amount","extra","tolls_amount","total_amount","time_stamp","weekday","month"]
em = []
mrh = []
arh = []
mn = []

for i in range(200):
    # time.sleep(2)
    m1 = []
    m2 = []
    m3 = []
    m4 = []
    pku = rd.randint(1, 263)
    den = rd.randint(1, 263)
    # mm = rd.randint(0, 143)
    wd = rd.randint(1, 7)
    pku_ll = "null"
    den_ll = "null"
    while den == pku:
        den = rd.randint(1, 263)
    for ii in mpp:
        if ii[0] == str(pku):
            pku_ll = ii[4]
            # print(ii[4])
    for ii in mpp:
        if ii[0] == str(den):
            den_ll = ii[4]
            # print(ii[4])
    pkus = pku_ll.replace(" ", "")
    dens = den_ll.replace(" ", "")
    url = req + pkus + "&destinations=" + dens + key
    response = urllib.request.urlopen(url)
    website = json.loads(response.read())
    m1.append(0)
    m1.append(0)
    m1.append((website['rows'][0]['elements'][0]['duration']['value']))  # get the trip_duration
    m1.append(website['rows'][0]['elements'][0]['distance']['text'].split()[0])  # get the trip_distance
    m1.append(0)    # ratecodeID
    m1.append(pku)
    m1.append(den)
    m1.append(0)    # fare amount
    m1.append(0)    # extra
    m1.append(0)    # tolls_amount
    m1.append(0)    # total_amount
    m1.append(rd.randint(24, 36))
    m1.append(wd)
    m2.append(0)
    m2.append(0)
    m2.append((website['rows'][0]['elements'][0]['duration']['value'])) # get the trip_duration
    m2.append(website['rows'][0]['elements'][0]['distance']['text'].split()[0]) # get the trip_distance
    m2.append(0)    # ratecodeID
    m2.append(pku)
    m2.append(den)
    m2.append(0)    # fare amount
    m2.append(0)    # extra
    m2.append(0)    # tolls_amount
    m2.append(0)    # total_amount
    m2.append(rd.randint(48, 60))
    m2.append(wd)
    m3.append(0)
    m3.append(0)
    m3.append((website['rows'][0]['elements'][0]['duration']['value'])) # get the trip_duration
    m3.append(website['rows'][0]['elements'][0]['distance']['text'].split()[0]) # get the trip_distance
    m3.append(0)    # ratecodeID
    m3.append(pku)
    m3.append(den)
    m3.append(0)    # fare amount
    m3.append(0)    # extra
    m3.append(0)    # tolls_amount
    m3.append(0)    # total_amount
    m3.append(rd.randint(96, 114))
    m3.append(wd)
    m4.append(0)
    m4.append(0)
    m4.append((website['rows'][0]['elements'][0]['duration']['value'])) # get the trip_duration
    m4.append(website['rows'][0]['elements'][0]['distance']['text'].split()[0]) # get the trip_distance
    m4.append(0)    # ratecodeID
    m4.append(pku)
    m4.append(den)
    m4.append(0)    # fare amount
    m4.append(0)    # extra
    m4.append(0)    # tolls_amount
    m4.append(0)    # total_amount
    m4.append(rd.randint(126, 138))
    m4.append(wd)
    m1.append(4)
    m2.append(4)
    m3.append(4)
    m4.append(4)
    em.append(m1)
    mrh.append(m2)
    arh.append(m3)
    mn.append(m4)

f = open(filename1, 'w', newline='')
csv_write = csv.writer(f)
csv_write.writerow(title)
for i in em:
    csv_write.writerow(i)

f = open(filename2, 'w', newline='')
csv_write = csv.writer(f)
csv_write.writerow(title)
for i in mrh:
    csv_write.writerow(i)

f = open(filename4, 'w', newline='')
csv_write = csv.writer(f)
csv_write.writerow(title)
for i in mn:
    csv_write.writerow(i)

f = open(filename3, 'w', newline='')
csv_write = csv.writer(f)
csv_write.writerow(title)
for i in arh:
    csv_write.writerow(i)




