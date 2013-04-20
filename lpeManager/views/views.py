from flask import request, session, g, redirect, url_for, \
                  render_template, flash
from flaskext.babel import refresh, gettext as _
from flask.ext.login import login_user, logout_user, current_user, login_required
from lpeManager import app, babel
from lpeManager.forms import LoginForm
from lpeManager.db import User
from lpeManager._version import __version__

@app.before_request
def before_request():
    g.version = __version__
    g.user = current_user
    if 'login' in request.path or 'static' in request.path:
        pass
    else:
        if not current_user.is_authenticated() and request.base_url != url_for('login'):
            return app.login_manager.unauthorized()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        flash(_("You're already logged, disconnect first"))
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None:
            flash(_('Username not found'))
            flash(_('Try again please'))
            return render_template('login.html',
                                   title = _('Sign In'),
                                   form = form,
                                  )
        elif user.check_password(form.password.data):
            login_user(user)
            flash(_('You are logged in'))
            return redirect(url_for('home'))
        else :
            flash(_('Wrong password'))
            flash(_('Try again please'))
            return render_template('login.html',
                                   title = _('Sign In'),
                                   form = form,
                                  )
    return render_template('login.html',
                           title = _('Sign In'),
                           form = form,
                          )

@app.route("/logout")
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('home'))

@app.route('/')
def home():
    return redirect(url_for('list_members'))


@babel.localeselector
def get_locale():
    user = getattr(g, 'user', None)
    if user.is_authenticated():
        return user.lang.label
    return request.accept_languages.best_match(['fr', 'en'])
