from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, Email, ValidationError
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

 