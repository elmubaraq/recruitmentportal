from portal import db, login_manager, bcrypt
from flask_login import UserMixin
from datetime import datetime



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email_address = db.Column(db.String(length=58),unique=True, nullable=False)
    password_hash= db.Column(db.String(length=60), nullable=False) 
    application = db.relationship('Application', backref='applicant', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
        
    def check_password_correlation(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
    
    def __repr__(self):
        return f'Item {self.email_address}'
    

    
class Application(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(80),unique=False, nullable=False)
    middle_name = db.Column(db.String(80),unique=False, nullable=False)
    last_name = db.Column(db.String(80),unique=False, nullable=False)
    home_town = db.Column(db.String(80),unique=False, nullable=False)     
    permanent_address = db.Column(db.String(80),unique=False, nullable=False) 
    town_of_residence = db.Column(db.String(80),unique=False, nullable=False)
    residential_address = db.Column(db.String(80),unique=False, nullable=False) 
    state_of_residence = db.Column(db.String(80),unique=False, nullable=False)
    state_of_origin = db.Column(db.String(80),unique=False, nullable=False)
    lga = db.Column(db.String(80),unique=False, nullable=False) 
    phone = db.Column(db.String(80),unique=False, nullable=False)
    nin = db.Column(db.String(10),unique=False, nullable=False)
    gender = db.Column(db.String(80),unique=False, nullable=False)
    primary_school = db.Column(db.String(80),unique=False, nullable=False)
    secondary_school = db.Column(db.String(80),unique=False, nullable=False)
    tertiary_school = db.Column(db.String(80),unique=False, nullable=False)
    highest_qualification = db.Column(db.String(80),unique=False, nullable=False)
    position_applying_for = db.Column(db.String(80),unique=False, nullable=False)
    passport_photo = db.Column(db.String(120),unique=False, nullable=False)
    birth_cert = db.Column(db.String(120),unique=False, nullable=False)
    school_cert = db.Column(db.String(120),unique=False, nullable=False)
    ssce_photo = db.Column(db.String(120),unique=False, nullable=False)
    tertiary_cert = db.Column(db.String(120),unique=False, nullable=False)
    nysc_cert = db.Column(db.String(120),unique=False, nullable=False)
    professional_cert = db.Column(db.String(120),unique=False, nullable=False)
    other_cert = db.Column(db.String(120),unique=False, nullable=False)
    owner = db.Column(db.String(80),db.ForeignKey('user.email_address'))
class test(db.Model):
    id = db.Column(db.Integer(), primary_key =True)
    name = db.Column(db.String(60), nullable = False, unique = True)
    data = db.Column(db.LargeBinary(),nullable = False)
    