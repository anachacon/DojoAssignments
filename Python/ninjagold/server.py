from flask import Flask, render_template, request, redirect, session
import datetime
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
    time = datetime.datetime.utcnow().replace(microsecond=0)

    if request.form["building"] == "farm":
        winnings = random.randrange(10, 20)
        session['gold'] = session.get('gold') + winnings
        activity.append("You earned "+str(winnings)+" golds from the farm! ("+str(time)+")")

    if request.form["building"] == "cave":
        winnings = random.randrange(5, 10)
        session['gold'] = session.get('gold') + winnings
        activity.append("You earned "+str(winnings)+" golds from the cave!")

    if request.form["building"] == "house":
        winnings = random.randrange(2, 5)
        session['gold'] = session.get('gold') + winnings
        activity.append("You earned "+str(winnings)+" golds from the house!")

    if request.form["building"] == "casino":
         print("casino")

    return redirect('/')

app.run(debug=True)