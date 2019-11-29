from map import db


class User(db.Model):  
	id = db.Column(db.Integer, primary_key=True) 
	name = db.Column(db.String(20))  


class Trip(db.Model):  
	id = db.Column(db.Integer, primary_key=True) 
	start = db.Column(db.Integer)  
	destination= db.Column(db.Integer)
	time = db.Column(db.String(100))