from map import db


class User(db.Model):  
	id = db.Column(db.Integer, primary_key=True) 
	name = db.Column(db.String(20))  


class Trip(db.Model):  
	id = db.Column(db.Integer, primary_key=True)
	duration = db.Column(db.Integer)
	distance = db.Column(db.Integer)
	start = db.Column(db.Integer)  
	destination= db.Column(db.Integer)
	timeStamp = db.Column(db.Integer)
	weekday = db.Column(db.Integer)
	month = db.Column(db.Integer)
	time = db.Column(db.String(100))
	price = db.Column(db.Integer)