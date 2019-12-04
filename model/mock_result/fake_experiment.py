import numpy as np
import random
import pandas

# price compare expriment #1 
uber = []
taxi = []
for i in range(10000):
	cur_int = random.randint(8,200)
	uber_item = round(random.uniform(cur_int - 3, cur_int + 3), 2)
	taxi_item = round(random.uniform(cur_int - 3, cur_int + 3), 2)
	uber.append(uber_item)
	taxi.append(taxi_item)

df = pandas.DataFrame(data={"uber_cost": uber, "taxi_cost": taxi})
df.to_csv("./cost_10000.csv", sep=',',index=False)

# with open("uber_cost.csv", 'w', newline='') as uber_cost:
#      wr = csv.writer(uber_cost, quoting=csv.QUOTE_ALL)
#      wr.writerow(uber)

# with open("taxi_cost.csv", 'w', newline='') as taxi_cost:
#      wr = csv.writer(taxi_cost, quoting=csv.QUOTE_ALL)
#      wr.writerow(taxi)


# fake for month data

for i in range(12):
	cur_uber = []
	cur_taxi = []
	for j in range(1000):
		cur_int = random.randint(8,200)
		uber_item = round(random.uniform(cur_int - 3, cur_int + 3), 2)
		taxi_item = round(random.uniform(cur_int - 3, cur_int + 3), 2)
		cur_uber.append(uber_item)
		cur_taxi.append(taxi_item)

	df = pandas.DataFrame(data={"uber_cost": cur_uber, "taxi_cost": cur_taxi})
	fileName = "./cost_month_" + str(i+1) + ".csv"
	df.to_csv(fileName, sep=',',index=False)


# peak hour
cur_uber = []
cur_taxi = []
for j in range(1000):
	cur_int = random.randint(15,250)
	uber_item = round(random.uniform(cur_int - 5, cur_int + 5), 2)
	taxi_item = round(random.uniform(cur_int - 5, cur_int + 5), 2)
	cur_uber.append(uber_item)
	cur_taxi.append(taxi_item)

df = pandas.DataFrame(data={"uber_cost": cur_uber, "taxi_cost": cur_taxi})
fileName = "./cost_peak_hour" + ".csv"
df.to_csv(fileName, sep=',',index=False)

# non peak hour
cur_uber = []
cur_taxi = []
for j in range(1000):
	cur_int = random.randint(15,150)
	uber_item = round(random.uniform(cur_int - 2, cur_int + 2), 2)
	taxi_item = round(random.uniform(cur_int - 2, cur_int + 2), 2)
	cur_uber.append(uber_item)
	cur_taxi.append(taxi_item)

df = pandas.DataFrame(data={"uber_cost": cur_uber, "taxi_cost": cur_taxi})
fileName = "./cost_non_peak_hour" + ".csv"
df.to_csv(fileName, sep=',',index=False)

#work day
cur_uber = []
cur_taxi = []
for j in range(1000):
	cur_int = random.randint(15,200)
	uber_item = round(random.uniform(cur_int - 4, cur_int + 4), 2)
	taxi_item = round(random.uniform(cur_int - 4, cur_int + 4), 2)
	cur_uber.append(uber_item)
	cur_taxi.append(taxi_item)

df = pandas.DataFrame(data={"uber_cost": cur_uber, "taxi_cost": cur_taxi})
fileName = "./cost_work_day" + ".csv"
df.to_csv(fileName, sep=',',index=False)


#workend
cur_uber = []
cur_taxi = []
for j in range(1000):
	cur_int = random.randint(18,240)
	uber_item = round(random.uniform(cur_int - 6, cur_int + 4), 2)
	taxi_item = round(random.uniform(cur_int - 6, cur_int + 4), 2)
	cur_uber.append(uber_item)
	cur_taxi.append(taxi_item)

df = pandas.DataFrame(data={"uber_cost": cur_uber, "taxi_cost": cur_taxi})
fileName = "./cost_workend" + ".csv"
df.to_csv(fileName, sep=',',index=False)