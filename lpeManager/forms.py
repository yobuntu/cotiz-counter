from flask.ext.wtf import Form, TextField, PasswordField
from wtforms import validators
from wtforms.ext.sqlalchemy.orm import model_form

from lpeManager.db import db, Member, Contribution

class LoginForm(Form):
    username = TextField('username')
    password = PasswordField('password')

MemberFormBase = model_form(Member, db.session, Form)

class MemberForm(MemberFormBase):
    def __init__(self, obj):
        super( MemberForm, self ).__init__()
        del self.contributions

ContributionForm = model_form(Contribution, db.session, Form)


class SimpleMemberForm(Form):
    pass
