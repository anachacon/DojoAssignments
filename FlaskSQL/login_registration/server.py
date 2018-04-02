from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import MySQLConnector 
import re
import md5, os, binascii
app = Flask(__name__)
app.secret_key = "my secret key"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, "loginregistration")

@app.route("/")
def index():
    if "logged_id" in session:
        return redirect("/dashboard")
    return render_template("index.html")

@app.route("/user", methods=["POST"])
def users():
    form_data = request.form
    action = form_data["action"]
    if action == "register":
        errors = []
        first_name = form_data["first_name"]
        last_name = form_data["last_name"]
        email = form_data["email"]
        password = form_data["password"]
        passwordconf = form_data["passwordconf"]
        
        if len(first_name) == 0:
            errors.append("First name cannot be blank")
        elif len(first_name) < 3:
            errors.append("First name has to be at least 3 characters")
        if len(last_name) == 0:
            errors.append("Last name cannot be blank")
        elif len(last_name) < 3:
            errors.append("First name has to be at least 3 characters")
        if len(email) == 0:
            errors.append("Email cannot be blank")
        elif not EMAIL_REGEX.match(email):
            errors.append("Email is not valid")
        if len(password) == 0:
            errors.append("Password cannot be blank")    
        elif len(password) <  8:
            errors.append("Password must be at least 8 characters")
        if len(passwordconf) == 0:
            errors.append("Password confirmation cannot be blank")    
        elif len(passwordconf) <  8:
            errors.append("Password confirmation must be at least 8 characters")
        elif password != password:
            errors.append("Passwords do not match")

        if len(errors) == 0:
            query = "SELECT id FROM users WHERE email = :email"
            data = {
                'email': request.form['email']
            }
            if len(mysql.query_db(query, data)) == 0:
                salt =  binascii.b2a_hex(os.urandom(15))
                hashed_pw = md5.new(password + salt).hexdigest()
                query = "INSERT INTO `users` (`first_name`, `last_name`, `email`, `password`, `salt`, `created_at`, `updated_at`) VALUES (:slot_one, :slot_two, :slot_three, :slot_four, :slot_five, now(), now());"
                data = {
                    "slot_one":first_name,
                    "slot_two":last_name,
                    "slot_three":email,
                    "slot_four":hashed_pw,
                    "slot_five": salt,
                }
                mysql.query_db(query, data)
                flash("Successful registration")
                return redirect("/success")
            else:
                flash("Email already exists")
                return redirect('/')
        else:
            for message in errors:
                flash(message)
            return redirect("/")
    elif action == "login":
        email = form_data["email"]
        password = form_data["password"]
        query = "SELECT * FROM users WHERE email=:email"
        data = {
                "email":email
            }
        user = mysql.query_db(query, data)
        if len(user) == 0:
            flash("Username does not exist")
            return redirect("/")
        else: 
            encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
            if user[0]["password"] == encrypted_password:
                flash("Successful login")
                return redirect("/success")
            else:
                flash("Incorrect password")
                return redirect("/")

@app.route("/success")
def success():
    return render_template("success.html")

app.run(debug=True)