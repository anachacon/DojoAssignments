from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ninja")
def ninja():
    url = "/static/img/tmnt.png"
    return render_template('index.html', url = url)

@app.route("/ninja/<name>")
def ninjas(name):
    if name == "blue":
        url = "/static/img/leonardo.jpg"
    elif name == "red":
        url = "/static/img/raphael.jpg"
    elif name == "orange":
        url = "/static/img/michelangelo.jpg"
    elif name == "purple":
        url = "/static/img/donatello.jpg"
    else:
        url = "/static/img/notapril.jpg"
    return render_template('index.html', url = url)
app.run(debug=True)