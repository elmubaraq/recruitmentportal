from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField
from wtforms.validators import Length, EqualTo, DataRequired, Email, ValidationError
from flask_wtf.file import FileAllowed, FileRequired
from portal.models import User


class RegistrationForm(FlaskForm):
    def validate_email_address(self,email_to_check):
        email = User.query.filter_by(email_address=email_to_check.data).first()
        if email:
            raise ValidationError('Email already exist, try forget password')
    email_address = StringField(label='Email:', validators=[Email(),DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=8),DataRequired()])
    password2 = PasswordField(label='Verify password', validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Create account')
    
class ApplicationForm(FlaskForm):
    first_name = StringField(label="First Name", validators=[DataRequired()])
    middle_name = StringField(label="Middle Name", validators=[DataRequired()])
    last_name = StringField(label="Last Name", validators=[DataRequired()])
    home_town = StringField(label="Home Town",validators=[DataRequired()])
    permanent_address = StringField(label="Permanent Address", validators=[DataRequired()])
    town_of_residence = StringField(label="Residential Town", validators=[DataRequired()])
    residential_address = StringField(label="Residential Address", validators=[DataRequired()])
    lga = StringField(label="Local Govt of Origin", validators=[DataRequired()])
    phone = StringField(label="Phone Number", validators=[DataRequired()])
    nin = StringField(label="NIN", validators=[DataRequired(), Length(min=10,max=10)])
    gender = SelectField(label="Gender", choices=[('1','MALE'),('2','FEMALE')])
    primary_school = StringField(label="Primary School Attended", validators=[DataRequired()])
    secondary_school = StringField(label= "Secondary School Attended", validators=[DataRequired()])
    tertiary_school = StringField(label= "Tertiary institution attended", validators=[DataRequired()])
    highest_qualification = SelectField(label="Highest Qualification", choices=[('1','SSCE'),('2','Diploma'),('3','Degree/HND'),('4','Second Degree'),('5','Third Degree')])
    passport_photo = FileField('Passport Photograph', validators=[FileRequired(), FileAllowed(['jpg','jpeg'], 'jpeg/jpg files only!')])
    birth_cert = FileField('Image',validators=[FileRequired(), FileAllowed(['jpg','jpeg'], 'jpeg/jpg files only!')])
    tertiary_cert = FileField('Higher Institution Cert. PDF!', validators=[FileRequired(), FileAllowed(['pdf'], 'PDF files only!')])
    other_cert = FileField('Other Certificates PDF!', validators=[FileAllowed(['pdf'], 'PDF files only!')])
    position_applying_for = SelectField(label="Position applying for", choices=[('1','Accountant I'),('2','Customer Service'),('3','Driver'),('4','Human Resource'),('5','Product Manager'),('6','Software Enginner (Backend) '),('7','Executive Assitant II')])
    professional_cert = FileField('Professional Certificates PDF!', validators=[FileAllowed(['pdf'], 'PDF files only!')])
    nysc_cert = FileField('NYSC Discharge/Exeption Cert. PDF', validators=[FileRequired(), FileAllowed(['pdf'], 'PDF files only!')])
    ssce_photo = FileField('SSCE Result JPG/JPEG', validators=[FileRequired(), FileAllowed(['jpg','jpeg'], 'jpeg/jpg files only!')])
    school_cert_photo = FileField('Primary School Cert. JPG/JPEG', validators=[FileRequired(), FileAllowed(['jpg','jpeg'], 'jpeg/jpg files only!')])
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
    
    

 