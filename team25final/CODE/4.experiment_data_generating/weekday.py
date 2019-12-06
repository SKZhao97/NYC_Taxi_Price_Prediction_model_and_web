from csv import reader
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
# generate 2 csv file
req = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="
key = "&key=your_key"
raw_map = "projection.csv"
filename1 = "weekday.csv"
filename2 = "weekend.csv"

# load the project.csv as list
mpp = list(reader(open(raw_map, 'rt'), delimiter=','))
del mpp[0]

title = ["pickup_location","dropoff_location","trip_duration","trip_distance","RatecodeID","PULocationID"
        ,"DOLocationID","fare_amount","extra","tolls_amount","total_amount","time_stamp","weekday","month"]
month3 = []
month6 = []

for i in range(200):
    # time.sleep(2)
    m3 = []
    m6 = []
    pku = rd.randint(1, 263)
    den = rd.randint(1, 263)
    # mm = rd.randint(0, 143)
    wd1 = rd.randint(1, 5)
    wd2 = rd.randint(6, 7)
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
    m3.append(0)
    m3.append(0)
    m3.append((website['rows'][0]['elements'][0]['duration']['value']))  # get the trip_duration
    m3.append(website['rows'][0]['elements'][0]['distance']['text'].split()[0])  # get the trip_distance
    m3.append(0)    # ratecodeID
    m3.append(pku)
    m3.append(den)
    m3.append(0)    # fare amount
    m3.append(0)    # extra
    m3.append(0)    # tolls_amount
    m3.append(0)    # total_amount
    m3.append(rd.randint(0, 143))
    m3.append(wd1)
    m6.append(0)
    m6.append(0)
    m6.append((website['rows'][0]['elements'][0]['duration']['value'])) # get the trip_duration
    m6.append(website['rows'][0]['elements'][0]['distance']['text'].split()[0]) # get the trip_distance
    m6.append(0)    # ratecodeID
    m6.append(pku)
    m6.append(den)
    m6.append(0)    # fare amount
    m6.append(0)    # extra
    m6.append(0)    # tolls_amount
    m6.append(0)    # total_amount
    m6.append(rd.randint(0, 143))
    m6.append(wd2)
    month3.append(m3)
    month6.append(m6)

f = open(filename1, 'w', newline='')
csv_write = csv.writer(f)
csv_write.writerow(title)
for i in month3:
    csv_write.writerow(i)

f = open(filename2, 'w', newline='')
csv_write = csv.writer(f)
csv_write.writerow(title)
for i in month6:
    csv_write.writerow(i)

