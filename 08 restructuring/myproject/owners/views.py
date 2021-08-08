from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_blueprint = Blueprint("owners",__name__, template_folder='templates/owners')

@owners_blueprint.route("/add",methods=['GET', 'POST'])
def add_owner():
    form = AddForm()
    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        add_owner = Owner(name,id)
        db.session.add(add_owner)
        db.session.commit()
        return redirect(url_for('add_owner'))
    return render_template('owner.html',form=form)