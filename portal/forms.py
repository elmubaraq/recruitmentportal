from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, DateField
from wtforms.validators import Length, EqualTo, DataRequired, Email, ValidationError
from flask_wtf.file import FileAllowed, FileRequired
from portal.models import User


class RegistrationForm(FlaskForm):
    def validate_email_address(self,email_to_check):
        email = User.query.filter_by(email_address=email_to_check.data).first()
        if email:
            raise ValidationError('Email already exist, try forget password')
    email_address = StringField(label='Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Verify password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create account')
class loginForm(FlaskForm):
    email_address = StringField(label='Email:', validators=[Email(),DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')
    
    
class ApplicationForm(FlaskForm):
    first_name = StringField(label="First Name", validators=[DataRequired(message="first name")])
    middle_name = StringField(label="Middle Name", validators=[DataRequired(message="middle name")])
    last_name = StringField(label="Last Name", validators=[DataRequired(message="last name")])
    home_town = StringField(label="Home Town",validators=[DataRequired(message="home town")])
    permanent_address = StringField(label="Permanent Address", validators=[DataRequired()])
    town_of_residence = StringField(label="Residential Town", validators=[DataRequired()])
    residential_address = StringField(label="Residential Address", validators=[DataRequired(message="Residential area not filled")])
    lga = StringField(label="Local Govt of Origin", validators=[DataRequired(message="Local govt Area not filled")])
    phone = StringField(label="Phone Number", validators=[DataRequired(message="Phone Number missing")])
    nin = StringField(label="NIN", validators=[DataRequired(message="NIN Required"), Length(min=10,max=10)])
    dob =  DateField(label="Date of Birth", validators=[DataRequired(message="date of birth")])
    gender = SelectField(label="Gender", choices=[('1','MALE'),('2','FEMALE')])
    primary_school = StringField(label="Primary School Attended", validators=[DataRequired(message="primary  school attended")])
    secondary_school = StringField(label= "Secondary School Attended", validators=[DataRequired(message="Secondary  School attended")])
    tertiary_school = StringField(label= "Tertiary institution attended", validators=[DataRequired(message="Institution attended")])
    highest_qualification = SelectField(label="Highest Qualification", validators=[DataRequired(message="highest qualification")],choices=[('1','SSCE'),('2','Diploma'),('3','Degree/HND'),('4','Second Degree'),('5','Third Degree')])
    passport_photo = FileField('Passport Photograph', validators=[ DataRequired(message="passport photo"), FileAllowed([ 'pdf','jpeg','jpg'], 'pdf/jpeg/jpg files only!')])
    birth_cert = FileField('Birth cert',validators=[ DataRequired(message="birth cert"), FileAllowed([ 'pdf','jpeg','jpg'], 'pdf/jpeg/jpg files only!')])
    tertiary_cert = FileField('Higher Institution Cert. PDF!', validators=[ DataRequired(message="Higher institution cert"), FileAllowed(['pdf'], 'pdf/jpeg/jpg files only!')])
    other_cert = FileField('Other Certificates PDF!', validators=[DataRequired(message="other cert"),FileAllowed([ 'pdf','jpeg','jpg'], 'pdf/jpeg/jpg files only!')])
    position_applying_for = SelectField(label="Position applying for", validators=[DataRequired(message="Position applying for")],choices=[('1','Accountant I'),('2','Customer Service'),('3','Driver'),('4','Human Resource'),('5','Product Manager'),('6','Software Enginner (Backend) '),('7','Executive Assitant II')])
    professional_cert = FileField('Professional Certificates PDF!', validators=[FileAllowed([ 'pdf','jpeg','jpg'], 'pdf/jpeg/jpg files only!')])
    nysc_cert = FileField('NYSC Discharge/Exeption Cert. PDF', validators=[ DataRequired(message="nysc cert"), FileAllowed([ 'pdf','jpeg','jpg'], 'pdf/jpeg/jpg files only!')])
    ssce_photo = FileField('SSCE Result JPG/JPEG', validators=[ DataRequired(message="ssce photo"), FileAllowed([ 'pdf','jpeg','jpg'], 'pdf/jpeg/jpg files only!')])
    school_cert_photo = FileField('Primary School Cert. JPG/JPEG', validators=[ DataRequired(message="school cert photo"), FileAllowed([ 'pdf','jpeg','jpg'], 'pdf/jpeg/jpg files only!')])
    state_of_residence = SelectField(label="State of Residence", choices=[('1','ABUJA FCT'),
                                                ('2','ABIA'),
                                                ('3','ADAMAWA'),
                                                ('4','AKWA IBOM'),
                                                ('5','ANAMBRA'),
                                                ('6','BAUCHI'),
                                                ('7','BAYELSA'),
                                                ('8','BENUE'),
                                                ('9','BORNO'),
                                                ('10','CROSS RIVER'),
                                                ('11','DELTA'),
                                                ('12','EBONYI'),
                                                ('13','EDO'),
                                                ('14','EKITI'),
                                                ('15','ENUGU'),
                                                ('16','GOMBE'),
                                                ('17','IMO'),
                                                ('18','JIGAWA'),
                                                ('19','KADUNA'),
                                                ('20','KANO'),
                                                ('21','KATSINA'),
                                                ('22','KEBBI'),
                                                ('23','KOGI'),
                                                ('24','KWARA'),
                                                ('25','LAGOS'),
                                                ('26','NASSARAWA'),
                                                ('27','NIGER'),
                                                ('28','OGUN'),
                                                ('29','ONDO'),
                                                ('30','OSUN'),
                                                ('31','OYO'),
                                                ('32','PLATEAU'),
                                                ('33','RIVERS'),
                                                ('34','SOKOTO'),
                                                ('35','TARABA'),
                                                ('36','YOBE'),
                                                ('37','ZAMFARA')], validators=[DataRequired()])
    state_of_origin = SelectField(label="State of origin", choices=[('1','ABUJA FCT'),
                                                ('2','ABIA'),
                                                ('3','ADAMAWA'),
                                                ('4','AKWA IBOM'),
                                                ('5','ANAMBRA'),
                                                ('6','BAUCHI'),
                                                ('7','BAYELSA'),
                                                ('8','BENUE'),
                                                ('9','BORNO'),
                                                ('10','CROSS RIVER'),
                                                ('11','DELTA'),
                                                ('12','EBONYI'),
                                                ('13','EDO'),
                                                ('14','EKITI'),
                                                ('15','ENUGU'),
                                                ('16','GOMBE'),
                                                ('17','IMO'),
                                                ('18','JIGAWA'),
                                                ('19','KADUNA'),
                                                ('20','KANO'),
                                                ('21','KATSINA'),
                                                ('22','KEBBI'),
                                                ('23','KOGI'),
                                                ('24','KWARA'),
                                                ('25','LAGOS'),
                                                ('26','NASSARAWA'),
                                                ('27','NIGER'),
                                                ('28','OGUN'),
                                                ('29','ONDO'),
                                                ('30','OSUN'),
                                                ('31','OYO'),
                                                ('32','PLATEAU'),
                                                ('33','RIVERS'),
                                                ('34','SOKOTO'),
                                                ('35','TARABA'),
                                                ('36','YOBE'),
                                                ('37','ZAMFARA')], validators=[DataRequired()])
    submit = SubmitField(label='Submit Application')
    
    

 