from flask import Flask, render_template, session, redirect, request, flash
import re
from mysqlconnection import MySQLConnector 
app = Flask(__name__)
app.secret_key = "my secret key"
mysql = MySQLConnector(app, "emailvalidation")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route("/")
def index():
    query = "SELECT * FROM emails"                           
    friends = mysql.query_db(query)                      
    return render_template('index.html', all_friends=friends) 

@app.route('/addemail', methods=['POST'])
def create():
    if len(request.form['email']) < 1:
        flash("Email cannot be empty!") #Check for empty input
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else: #Check for existing email - if not existing insert into database
        query = "SELECT id FROM emails WHERE address = :address"
        data = {
            'address': request.form['email']
        }
        print (mysql.query_db(query, data))
        if len(mysql.query_db(query, data)) == 0:
            insertquery = "INSERT INTO emails (address, created_at, updated_at) VALUES (:address, NOW(), NOW())"
            data = {
             'address': request.form['email']
            }
            mysql.query_db(insertquery, data)
            session['email'] = request.form['email']
            return redirect('/success')
        else:
            flash("Email already exists")
    return redirect('/')

@app.route("/success")
def success():
    query = "SELECT * FROM emails"                           
    friends = mysql.query_db(query)                      
    return render_template('success.html', all_friends=friends) 


app.run(debug=True)