from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import MySQLConnector 
app = Flask(__name__)
app.secret_key = "my secret key"
mysql = MySQLConnector(app, "friends")

@app.route("/")
def index():
    query = "SELECT * FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our templatecopy

@app.route('/addfriend', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'name': request.form['name'],
             'age':  request.form['age']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)