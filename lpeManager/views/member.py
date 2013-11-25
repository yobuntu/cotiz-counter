from flask import request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify
from flaskext.babel import gettext as _, format_datetime

from lpeManager import app
from lpeManager.db import Member, db
from lpeManager.forms import MemberForm


@app.route('/members/list', methods=['GET','POST'])
def member_list():
    members = Member.query.all()
    member = Member()
    form = MemberForm(obj=member)
    if form.validate_on_submit():
        form.populate_obj(member)
        db.session.add(member)
        db.session.commit()
        flash(_("Member {0} added").format(member.username))
        return redirect(url_for('member_list'))
    return render_template('/member/list.html', form=form, members=members)

@app.route('/inscription/new', methods=['GET','POST'])
def inscription():
    member = Member()
    form = SimpleMemberForm(obj=member)
    if form.validate_on_submit():
        form.populate_obj(member)
        db.session.add(member)
        db.session.commit()
        flash(_("Your are now registred, we are waiting for your fee to grant you full access"))
        return redirect(url_for('inscription_complete'))
    return render_template('/member/inscription.html', form=form)

@app.route('/inscription/complete')
def inscription_complete():
    return render_template('/member/inscription_complete.html')
