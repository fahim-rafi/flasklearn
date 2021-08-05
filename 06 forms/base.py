from flask import Flask, request, url_for, render_template, flash, session, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'openkey'

class SimpleForm(FlaskForm):
    breed = StringField("What breed of pups are you looking for?")
    submit = SubmitField("Submit")

@app.route('/', methods=['GET', 'POST'])
def index():
    breed = False
    form = SimpleForm()
    if form.validate_on_submit():
        session["breed"] = form.breed.data
        flash('You have submitted the breed!')
    return render_template('index.html', form=form, breed=breed)

if __name__ == '__main__':
    app.run(debug=True)