from flask import Flask
#pip install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
#now, lets set a URL for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'
#then use the application object as a parameter to create an object of class SQLAlchemy
db=SQLAlchemy(app)
app.config["SECRET_KEY"]='bdfbcdc502722bc56058y1d0'
from portal.models import User