from flask import Flask
#pip install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate


app=Flask(__name__)
#now, lets set a URL for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databank.db'
#then use the application object as a parameter to create an object of class SQLAlchemy
db=SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message = 'Please register and login before you continue with you application!'
login_manager.login_message_category = 'info'
app.config["SECRET_KEY"]='bdfbcdc502722bc56058y1d0'
app.config['UPLOAD_FOLDER'] = 'portal/static/uploads'
from portal.models import User, Application, test
