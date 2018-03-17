from flask import Flask, render_template, request, redirect, session
from datetime import datetime as dt
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route("/")
def index():
    if not session.get('gold'):
        session['gold'] = 0
        session['activity'] = []
    print(session.get('activity'))
    return render_template("index.html", gold = session.get('gold'))
    
@app.route("/process_money", methods=["POST"])
def process():
    activity = session.get('activity')
    time = dt.strftime(dt.now(), "%Y/%m/%d, %I:%M %p")
    # time = dt.utcnow().replace(microsecond=0)

    if request.form["building"] == "farm":
        winnings = random.randrange(10, 20)
        session['gold'] = session.get('gold') + winnings
        activity.append("You earned "+str(winnings)+" golds from the farm! ("+str(time)+")")
        # session.modified = True

    if request.form["building"] == "cave":
        winnings = random.randrange(5, 10)
        session['gold'] = session.get('gold') + winnings
        activity.append("You earned "+str(winnings)+" golds from the cave!")
        # session.modified = True

    if request.form["building"] == "house":
        winnings = random.randrange(2, 5)
        session['gold'] = session.get('gold') + winnings
        activity.append("You earned "+str(winnings)+" golds from the house!")
        # session.modified = True

    if request.form["building"] == "casino":
        print("casino")
        # session.modified = True

    return redirect('/')

app.run(debug=True)