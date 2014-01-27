from flask.ext.wtf import Form, TextField, PasswordField
from wtforms import validators
from wtforms.ext.sqlalchemy.orm import model_form

from lpeManager.db import db, Member, Contribution

class Hider(object):
    def __get__(self,instance,owner):
        raise AttributeError, "Hidden attrbute"

    def __set__(self, obj, val):
        raise AttributeError, "Hidden attribute"

class LoginForm(Form):
    username = TextField('username')
    password = PasswordField('password')

MemberFormBase = model_form(Member, db.session, Form)

class MemberForm(MemberFormBase):
    contributions = None

ContributionFormBase = model_form(Contribution, db.session, Form)

class ContributionForm(ContributionFormBase):
    member = None



class SimpleMemberForm(Form):
    pass
