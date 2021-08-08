# Importing libraries
import os
from flask import Flask
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
