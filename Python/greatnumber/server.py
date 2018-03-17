from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route("/")
def index():
    if not session.get('number'):
        session['number'] = random.randrange(0, 101) 
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    guess = int(request.form["guess"])
    number = session.get('number')
    print(number)
    if guess > number:
        result = "Too high!"
    elif guess < number:
        result = "Too low!"
    else:
        result = "win"
        session.pop('number')
    return render_template("index.html", result = result, number=number)

app.run(debug=True)