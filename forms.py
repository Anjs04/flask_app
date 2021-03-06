from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter you last name.")])
    email = StringField('Email', validators=[DataRequired("Please enter a valid email address."), Email("Please enter a valid email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a valid password."), Length(min=6, message="Passwords must be at least 6 characters long.")])
    submit = SubmitField('Sign up')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter a valid email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a valid password."), Length(min=6, message="Passwords must be at least 6 characters long.")])
    submit = SubmitField('Log in')

class AddressForm(Form):
    address = StringField("Address", validators=[DataRequired()])
    submit = SubmitField('Search')
