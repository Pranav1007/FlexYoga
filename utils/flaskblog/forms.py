# Define all the Forms on Flask to accept User Data

from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, SelectField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, Length
from .model import User

class UserRegistration(FlaskForm):
    username = StringField('UserName', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email ID', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=7, max=15)])
    age = IntegerField('Age', validators=[DataRequired()])
    submit = SubmitField('Register')

    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        print(user)
        if user:
            raise ValidationError('Username taken. Please pick another one')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered.')

    def validate_age(self, age):
        if (age.data < 18 or age.data > 65):
            raise ValidationError('Only people within the age limit of 18-65 can enroll')

class LoginForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired(), Length(min=3, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=7, max=15)])
    submit = SubmitField("Login")

class MembershipForm(FlaskForm):
    batch = SelectField('Select Batch', validators=[DataRequired()], choices=[('6:00 AM to 7:00 AM'), ('7:00 AM to 8:00 AM'), ('8:00 AM to 9:00 AM'), ('5:00 PM to 6:00 PM')])
    confirm = SubmitField('Confirm and Pay')
