import json
from flask import url_for
from flask import render_template
from flask import request, redirect, flash

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
		# parameters = request.get_json(silent=True)
		data = request.get_json(force=True)
		# print("data is " + format(data))
		start = int(data["parameters"]['start'])
		destination = int(data["parameters"]['destination'])
		time = data["parameters"]["time"]
		result = start + destination
		global num
		# num = len(result)
		num = start + destination
		# print(num)

		trip = Trip (start = start, destination = destination, time = time)	## [Optional] Database operations
		db.session.add(trip)
		db.session.commit()

	return str(result)


@app.route('/getpythondata')	# GET route
def get_python_data():
	# print(num)
	num = calculate()
	return json.dumps(num)


def calculate():		# Test function, simulate the prediction model using simple addition
	global num
	num = num + 100
	return num
