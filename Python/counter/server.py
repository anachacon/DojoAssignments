from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route("/")
def index():
    if not session.get('counter'):
        session['counter'] = 1
    return render_template("index.html", counter=session['counter'])

@app.route("/process")
def process():
    counter = session.get('counter')
    counter += 2
    session['counter'] = counter
    return render_template("index.html", counter=session['counter'])

@app.route("/reset")
def reset():
    session['counter'] = 1
    return render_template("index.html", counter=session['counter'])

app.run(debug=True)