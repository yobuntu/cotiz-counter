from flask.ext.wtf import Form, TextField, PasswordField
from wtforms import validators
from wtforms.ext.sqlalchemy.orm import model_form

from lpeManager.db import db, Member, Contribution

class LoginForm(Form):
    username = TextField('username')
    password = PasswordField('password')

MemberForm = model_form(Member, db.session, Form)
ContributionForm = model_form(Contribution, db.session, Form)
