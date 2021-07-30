# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model 
import meme_lib

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        return "You didn't enter anything"
    else:
        # recommendations = request.form['recommendations']
        # if recommendations == "1":
        #     return model.outcome()
        # elif recommendations == "2":
        #     return
        # elif recommendations == "3":
        #     return "No recommendations!"
        user_mood=request.form["recommendations"]
        outcome_info = model.outcome(user_mood)
    return render_template("results.html", user_mood=user_mood, outcome_info=outcome_info)
    
