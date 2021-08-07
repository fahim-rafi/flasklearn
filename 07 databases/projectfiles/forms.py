from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField("What's the name of the pupper?&#160")
    submit = SubmitField("Add pupper!")

class DelForm(FlaskForm):
    id = IntegerField("What's the ID of the pupper?&#160")
    submit = SubmitField("Remove pupper!")

class OwnerForm(FlaskForm):
    id = IntegerField("What's the ID of the pupper?&#160")
    name = StringField("What's the name of the owner?&#160")
    submit = SubmitField("Add owner!")