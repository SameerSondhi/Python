from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.client_model import Client

# Bcrypt
bcrypt = Bcrypt(app) 

# Index route
@app.route("/")
def index():
    return render_template("index.html")

# Client registration with validation
@app.route("/clients/register", methods = ['POST'])
def reg_client():
    if not Client.validator(request.form):
        return redirect("/")
    hashed_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password' : hashed_pass,
        'conf_pass': hashed_pass
    }
    logged_client_id = Client.create(data)
    session['client_id'] = logged_client_id
    return redirect("/clients/success")


# Client success page after registering
@app.route("/clients/success")
def success():
    return render_template("success.html")


# Login for client
@app.route("/clients/login", methods = ['POST'])
def log_client():
    data = {
        'email': request.form['email']
    }
    client_in_db = Client.get_by_email(data)
    if not client_in_db:
        flash("Invalid credentials! Please try again!", "log")
        return redirect("/")
    if not bcrypt.check_password_hash(client_in_db.password, request.form['password']):
        flash("Invalid credentials! Please try again!", "log")
        return redirect("/")
    session['client_id'] = client_in_db.id
    return redirect('/dashboard')

# Logout route
@app.route("/clients/logout")
def logout():
    del session['client_id']
    return redirect("/")


# Dashboard
@app.route("/dashboard")
def dashboard():
    if 'client_id' not in session:
        return redirect("/")
    data = {
        'id' : session['client_id']

    }
    logged_client = Client.get_by_id(data)
    return render_template("welcome.html", logged_client = logged_client)
