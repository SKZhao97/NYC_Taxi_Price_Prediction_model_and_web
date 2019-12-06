# CSE6242 Final Project --Web application

## DESCRIPTION

Interactive web application to predict the price of Yellow Taxi of New York City based on FLASK framework. A regression model based on Microsoft lightGBM framework is trained using data of 2018(7.85G) and ingrained in the web back end. In the front end, Google map API is called to generate map, marker and get location. Distance matrix API is called to get estimated duration and distance. D3.js is used to transfer the longitude and latitude into NYC taxi zone. jQuery .Ajax is used to send data between two ends. SQLite database is embedded to store search history.

## INSTALLATION

$ pip install pandas
$ pip install lightgbm
$ pip install numpy
$ pip install sklearn

$ pip install pipenv
$ pipenv install --dev

## EXECUTION

$ pipenv shell
$ set FLASK_ENV=development (use export instead of set on MacOS)
$ set FLASK_APP=map (use export instead of set on MacOS)
$ flask initdb
$ flask run

$ Running on(local) http://127.0.0.1:5000/
$ Press CTRL+C to quit
