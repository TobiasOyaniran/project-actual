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
    if request.method == "POST":
        print("Method was POST")
        if request.form.get == ("rec_one"):
            return model.recommendation_one
        if request.form.get == ("rec_two"):
            return model.recommendation_two
        if request.form.get == ("rec_three"):
            return model.recommendation_three
    else:
        print("Methodd was GET")
    
    # if request.form["rec_one"]:
    #     return model.recommendation_one()
    # elif request.form["rec_two"]:
    #     return model.recommendation_two()
    # elif request.form["rec_three"]:
    #     return model.recommendation_three()
        