from flask import Flask, render_template, redirect, url_for, session, flash
from flask_wtf.csrf import CSRFProtect
from flask_login import login_user, login_required, current_user, LoginManager
from forms import LoginForm, RegisterForm
from models import db, User  # Import User from models.py
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
secret_key = os.environ.get("SECRET_KEY", "58d3b9a5efb4388ff3c5fd65fe853dcc38b808d739280b06")
app.config["SECRET_KEY"] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login'

csrf = CSRFProtect(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if user.check_password(password):
                login_user(user)
                flash("Login successful!", "success")
                return redirect(url_for("profile"))
            else:
                flash("Invalid email or password. Please try again.", "error")
        else:
            flash("User not found. Please check your email and try again.", "error")
    return render_template("login.html", form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('register'))
        
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('Email already exists. Please use a different one.', 'error')
            return redirect(url_for('register'))
        
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        flash('Registration successful! You are now signed in.', 'success')
        return redirect(url_for('profile'))
    
    return render_template('register.html', form=form)

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
