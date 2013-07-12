from flask import request, session, g, redirect, url_for, abort, render_template, flash
from flaskext.babel import gettext as _, format_datetime

from lpeManager import app
from lpeManager.db import Member, Contribution
from lpeManager.forms import ContributionForm

@app.route('/contributions/add',methods=['GET','POST'])
def add_contribution(member_id):
    pass

