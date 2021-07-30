import requests
from flask import Flask, render_template, url_for, flash, redirect, request
import forms
from util.auth_utils import *
from util.db_utils import *
from classes.classes import *
app = Flask(__name__)
app.config['SECRET_KEY'] = '766ad3b9779f8e26642e74331dbf694c'


@app.route("/")
def home():
    return render_template("home.html")
  


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    unsuccessful = "Make sure the passwords match"
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmed_password = request.form.get('confirmed_password')
        college = request.form.get('college')
        if password == confirmed_password:
            try:
                user = sign_up_user(email, password, name, college)
                return render_template("home.html")
            except:
                unsuccessful_register = "Something went wrong"
                return render_template("register.html", unsuccessful=unsuccessful)
        return render_template("register.html", unsuccessful=unsuccessful)
    return render_template("register.html")
   


@app.route("/login", methods=['GET', 'POST'])
def login():
    unsuccessful = "Check your email or password."
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = sign_in_user(email, password)
            return render_template("home.html")
        except:
            return render_template("login.html", unsuccessful=unsuccessful)
    
    return render_template("login.html")





if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")