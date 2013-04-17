from flask import Flask
from flask.ext.babel import Babel
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)

# import configuration
app.config.from_object('lpeManager.default_settings')
app.config.from_envvar('LPE_SETTINGS')

