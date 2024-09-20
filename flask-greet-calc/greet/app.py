# Simple flask app 

from flask import Flask
app = Flask(__name__)

# welcome route 
@app.route('/welcome')
def welcome():
    return 'Welcome'

# welcome home route
@app.route('/welcome/home')
def welcome_home():
    return 'Welcome home'

# welcome back route
@app.route('/welcome/back')
def welcome_back():
    return 'Welcome back'

