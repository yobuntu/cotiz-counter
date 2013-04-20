from flask import request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify
from flaskext.babel import gettext as _, format_datetime
from lpeManager import app
from lpeManager.db import Member, db

@app.route('/members/list')
def home():
    return render_template('/member/list.html')
