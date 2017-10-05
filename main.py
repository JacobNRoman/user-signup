from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template("signup.html")

@app.route('/', methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    name_err = ''
    pw_err = ''
    verify_err = ''
    email_err = ''
    period_count = 0
    a_count = 0

    if username == "":
        name_err = "You must enter a username"
    elif len(username) < 3 or len(username) > 20 or " " in username:
        name_err = "Username must be more than 3 characters and less than 20 and must contain no spaces"
    if password == "": 
        pw_err = "You must enter a password"
        password = ""
    elif len(password) < 3 or len(password) > 20 or " " in password:
        pw_err = "Password must be more than 3 characters and less than 20 and must contain no spaces"
        password = ""
    if password != verify:
        verify_err = "Passwords do not match"
        verify = ""
    if email != "":
        if len(email) < 3 or len(email) > 20 or " " in email:
            email_err = "A valid email must contain more than 3 characters and less than 20, and must contain no spaces"
        for char in email:
            if char == ".":
                period_count += 1
            if char == "@":
                a_count += 1
        if period_count != 1 or a_count != 1:
            email_err = 'A valid email contains one "." and one "@"'
    if not name_err and not email_err and not verify_err and not email_err:
        return redirect ("/welcome?name=" + username)
    else: 
        return render_template("signup.html", name_err=name_err, pw_err=pw_err, verify_err=verify_err, email_err=email_err, username=username, password=password, verify=verify, email=email)

@app.route("/welcome")
def welcome():
    name = request.args.get("name")
    return render_template("welcome.html", name=name)

app.run()