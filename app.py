# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model 

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/choose_activity", methods =["GET", "POST"])
def choose_activity():
    if model.recommendation_one:
        return "Choose an activity! We recommend browsing through some memes!"
    elif model.recommendation_two:
        return "Choose an activity! We recommend playing a minigame!"
    elif model.recommendation_three:
        return "Choose an activity!"
    
        