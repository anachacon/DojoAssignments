from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route("/")
def index():
    if not session.get('number'):
        session['number'] = random.randrange(0, 101)
    if session.get('result'):
        return (render_template("index.html", result = session.get('result'), number=session.get('number')))
    return render_template("index.html", result = "Take a guess")

@app.route('/process', methods=["POST"])
def process():
    guess = int(request.form["guess"])
    number = session.get('number')
    print(number)
    if guess > number:
        session['result'] = "Too high!"
    elif guess < number:
        session['result'] = "Too low!"
    else:
        session['result'] = "win"
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('number')
    session.pop('result')
    return redirect('/')
    
app.run(debug=True)