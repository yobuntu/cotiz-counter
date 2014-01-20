from flask import request, session, g, redirect, url_for, abort, render_template, flash
from flaskext.babel import gettext as _, format_datetime

from lpeManager import app
from lpeManager.db import db, Member, Contribution
from lpeManager.forms import ContributionForm

@app.route('/contributions/add/<member_id>',methods=['GET','POST'])
def add_contribution(member_id):
    contribution = Contribution()
    member = Member.query.filter_by(id=member_id).one()
    contribution.member = member
    form = ContributionForm(obj=contribution)
    if form.validate_on_submit():
        form.populate_obj(contribution)
        db.session.add(contribution)
        db.session.commit()
        flash(_("Contribution added for member"))
        return redirect(url_for('member_list'))
    return render_template('/contribution/add.html', form=form, member=member)

