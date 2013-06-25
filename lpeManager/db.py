from lpeManager import app
from flask.ext.bcrypt import check_password_hash, generate_password_hash
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
ROLE_USER = 1
ROLE_ADMIN = 2

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), unique = True)
    role_id = db.Column(db.SmallInteger, db.ForeignKey('role.id'), default=ROLE_USER)
    role = db.relationship("Role")
    lang_id = db.Column(db.SmallInteger, db.ForeignKey('lang.id'), default=1)
    lang = db.relationship("Lang")

    def __init__(self):
        pass
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User {0}>'.format(self.username)

    def set_password(self, raw_password):
        self.password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        """
        Returns a boolean of whether the raw_password was correct. Handles
        encryption formats behind the scenes.
        """
        return check_password_hash(self.password, raw_password)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    label = db.Column(db.String(15), unique = True)

    def __init__(self, label):
        self.label = label

    def __str__(self):
        return self.label

class Lang(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    label = db.Column(db.String(5), unique = True)

    def __init__(self, label):
        self.label = label

    def __str__(self):
        return self.label

class Member(db.Model):
    id = db.Column(db.Integer(unsigned=True), primary_key=True)
    firstname = db.Column(db.String(100))
    lastname  = db.Column(db.String(100))
    username  = db.Column(db.String(100), unique=True, nullable=False)
    email     = db.Column(db.String(100), nullable=False)
    reddit_account = db.Column(db.String(100), unique=True, nullable=False)
    inscription_date = db.Column(db.Date(), nullable=False)
    fee_ok    = db.Column(db.Boolean())
    account_ok = db.Column(db.Boolean())

    def expire_at(self):
        return self.inscription_date
    

