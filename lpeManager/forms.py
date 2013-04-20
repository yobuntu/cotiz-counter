from wtforms import validators
from flask.ext.wtf import Form, TextField, PasswordField

class LoginForm(Form):
    username = TextField('username')
    password = PasswordField('password')
