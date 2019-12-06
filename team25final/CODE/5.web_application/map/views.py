import json
from flask import url_for
from flask import render_template
from flask import request, redirect, flash
from datetime import datetime
import pandas as pd
import lightgbm as lgb
from sklearn.metrics import mean_squared_error
import numpy as np

from map import app, db
from map.models import User, Trip
num = 0;

@app.route('/')	# Home page
def index():
	return render_template('index.html')


@app.route('/test')	# Test route
def test():
	return "hello"


@app.route('/your/flask/endpoint', methods=['GET','POST'])	# POST route
def get_parameters():
	if request.method == 'POST':
		data = request.get_json(force=True)
		print(data)
		
		start = int(data["parameters"]['start'])
		destination = int(data["parameters"]['destination'])
		duration = int(data["parameters"]['duration'])
		distance = int(data["parameters"]['distance'])
		distance = distance/1610
		distance = round(distance,2)
		time = data["parameters"]["time"]
		x = datetime.strptime(time, '%H:%M %m/%d/%Y')
		timezone = time_zone(x.hour, x.minute)
		weekday = x.weekday()+1
		month = x.month

		result = start + destination
		global num
		num = start + destination

		print("duration------->" + str(duration))
		print("distance------->" + str(distance))
		print("start---------->" + str(start))
		print("destination---->" + str(destination))
		print("timezone------->" + str(timezone))
		print("weekday-------->" + str(weekday))
		print("month---------->" + str(month))

		df = pd.DataFrame(np.array([[duration,distance,start,destination,timezone,weekday,month]]))
		test = predict(df)
		num = round(test[0],2)
		price = num

		trip = Trip(duration=duration, distance=distance, start = start, destination = destination, timeStamp = timezone, weekday = weekday, month = month, time = time, price = price )	## [Optional] Database operations
		db.session.add(trip)
		db.session.commit()

	return str(result)


@app.route('/getpythondata')	# GET route
def get_python_data():
	global num
	print("Predicted fare--->"+ str(num))
	return json.dumps(num)

def time_zone(h, m):
	return h * 6 + m // 10

def calculate():		# Test function, simulate the prediction model using simple addition
	global num
	num = num + 100
	return num

def predict(X_test):
	#feature columns [2,3,5,6,11,12,13]
	print('Loading model to predict...')
	# load model to predict
	bst = lgb.Booster(model_file='./map/model.txt')
	# can only predict with the best iteration (or the saving iteration)
	y_pred = bst.predict(X_test)
	return y_pred
