from flask import Flask
from flask.ext.babel import Babel
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)


# import configuration
app.config.from_object('lpeManager.default_settings')
app.config.from_envvar('LPE_SETTINGS')

from lpeManager.db import User

# manage login
bcrypt = Bcrypt(app)
lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'login'
@lm.user_loader
def load_user(userid):
    return User.query.get(int(userid))

#i18n
babel = Babel(app)

from lpeManager.views import views, member, contribution
