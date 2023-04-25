from flask import Flask
#pip install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
#now, lets set a URL for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'
#then use the application object as a parameter to create an object of class SQLAlchemy
db=SQLAlchemy(app)

from portal.models import User