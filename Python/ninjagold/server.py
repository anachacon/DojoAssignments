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

    if request.form["building"] == "farm":
        winnings = random.randrange(10, 21)
        session['gold'] = session.get('gold') + winnings
        activity.append({
            "message": "Earned {} golds from the farm! ({})".format(winnings, time),
            "color":"green"
        })

    if request.form["building"] == "cave":
        winnings = random.randrange(5, 11)
        session['gold'] = session.get('gold') + winnings
        activity.append({
            "message": "Earned {} golds from the cave! ({})".format(winnings, time),
            "color":"green"
        })

    if request.form["building"] == "house":
        winnings = random.randrange(2, 6)
        session['gold'] = session.get('gold') + winnings
        activity.append({
            "message": "Earned {} golds from the house! ({})".format(winnings, time),
            "color":"green"
        })

    if request.form["building"] == "casino":
        game = random.randrange(0, 2)
        winnings = random.randrange(0, 51)
        if game == 0:
            session['gold'] = session.get('gold') - winnings
            activity.append({
            "message": "Entered a casino and lost {} golds... Ouch ({})".format(winnings, time),
            "color": "red"
             })
        else: 
            session['gold'] = session.get('gold') + winnings
            activity.append({
            "message": "Entered a casino and won {} golds! ({})".format(winnings, time),
            "color": "green"
             })

    return redirect('/')

app.run(debug=True)