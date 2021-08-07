# Importing libraries
import os
from flask import Flask, render_template, url_for, request
# from forms import AddForm, DelForm, OwnerForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initializing flask app
app = Flask(__name__)
# SECRET_KEY is specified directly temporarily
app.config["SECRET_KEY"] = "placeholder_key"

# Setting base directory and SQLite Database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app,db)

# Creating Tables
## Puppies table
class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref="puppy",uselist=False)
    
    def __init__(self,name,owner):
        self.name = name
    
    def __repr__(self):
        if self.owner:
            return f"{self.name} with an ID of {self.id} has been adopted by {self.owner}"
        else:
            return f"{self.name} with an ID of {self.id} has not been adopted yet! :( "

## Owners table
class Owner(db.Model):
    __tablename__ = "owners"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey("puppies.id"))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

# View forms
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add",methods=['GET', 'POST'])
def add_pup():
    return render_template('add.html')

@app.route("/del",methods=['GET', 'POST'])
def del_pup():
    return render_template('delete.html')

@app.route("/owner",methods=['GET', 'POST'])
def add_owner():
    return render_template('owner.html')

@app.route("/list")
def list_pup():
    return render_template('list.html')

if __name__ == '__main__':
    app.run(debug=True)
