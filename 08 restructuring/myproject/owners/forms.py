from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    id = IntegerField("What's the ID of the pupper?&#160")
    name = StringField("What's the name of the owner?&#160")
    submit = SubmitField("Add owner!")