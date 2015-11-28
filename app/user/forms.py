__author__='Dwi Sulfahnur'

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, validators
from models import User

class LoginForm(Form):
    username = StringField('username', [validators.DataRequired('Masukkan Username Anda')])
    password = PasswordField('password', [validators.DataRequired('Masukkan Password Anda')])   
