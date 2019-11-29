import os
import json
import click
from flask import Flask
from flask import url_for
from flask import render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy  

prefix = 'sqlite:////'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')	# database initiate
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# num = 0;	# Global variable

from map import views, errors, commands