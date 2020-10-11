from flask_sqlalchemy import SQLAlchemy
from main import App

App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/Database.db'
App.secret_key = "kJRlFT6PkZU5N"

db = SQLAlchemy(App)


class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user = db.Column(db.String(200))
	password = db.Column(db.String(200))

class Devices(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user = db.Column(db.String(200))
	password = db.Column(db.String(200))
	device_hash = db.Column(db.String(200))
	hostname = db.Column(db.String(200))
	ip = db.Column(db.String(200))
