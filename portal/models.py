from portal import db

class User(db.Model):
    id = db.Column( db.Integer(), primary_key=True)
    email_address = db.Column(db.String(length=58),unique=True, nullable=False)
    password_harsh= db.Column(db.String(length=60), nullable=False) 
        