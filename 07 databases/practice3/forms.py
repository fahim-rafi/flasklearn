from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField("Name of pupper: ")
    submit = SubmitField("Add pupper")

class DelForm(FlaskForm):
    id = IntegerField("ID of pupper to remove:")
    submit = SubmitField("Remove pupper")
