# Set up your imports here!
from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hi! This is my first attempt at flask.</h1>'

@app.route('/user/<name>') # Fill this in!
def user(name):
    capname = name[0].upper() +name[1:]
    return "<h1>Hi {}! Welcome to my flask web app!".format(capname)

if __name__ == '__main__':
    app.run(debug=True)