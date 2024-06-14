from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, current_user, LoginManager, logout_user
from models import db, User, init_db
import os
from flask_wtf.csrf import CSRFProtect
import requests
import random


app = Flask(__name__)
secret_key = os.environ.get("SECRET_KEY", "58d3b9a5efb4388ff3c5fd65fe853dcc38b808d739280b06")
app.config["SECRET_KEY"] = secret_key


# csrf token
csrf = CSRFProtect(app)


# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
init_db(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remember = request.form.get("remember")  # Check if "Remember Me" is checked
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user, remember=remember)  # Set remember parameter
            return redirect(url_for("profile"))
        else:
            flash("Login Unsuccessful. Please check email and password", 'danger')
    return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Check if the email or username already exists
        user_by_username = User.query.filter_by(username=username).first()
        user_by_email = User.query.filter_by(email=email).first()

        if user_by_username:
            flash("Username already exists!", category="danger")
        elif user_by_email:
            flash("Email already exists!", category="danger")
        elif len(email) < 4:
            flash("Email is too short!", category="danger")
        elif len(username) < 2:
            flash("Username is too short!", category="danger")
        elif password != confirm_password:
            flash("Passwords don't match!", category="danger")
        elif len(password) < 5:
            flash("Passwords must be greater than 4 characters", category="danger")
        else:
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!", category="success")
            login_user(new_user)  # Log in the user automatically
            return redirect(url_for("profile"))
    return render_template("register.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('index'))

@app.route("/profile")
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@app.route("/saved")
@login_required
def saved():
    return render_template("saved.html")



if __name__ == "__main__":
    app.run(debug=True)
