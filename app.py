from flask import Flask, render_template, redirect, url_for, session, flash
from flask_wtf.csrf import CSRFProtect
from flask_login import login_user, login_required, current_user, LoginManager
from forms import LoginForm, RegisterForm
from database import init_db, insert_user  # Import the insert_user function
from models import User, db, init_app
import os

 ## declare database
secret_key = os.environ.get("SECRET_KEY", "58d3b9a5efb4388ff3c5fd65fe853dcc38b808d739280b06")
app = Flask(__name__)
login_manager = LoginManager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
app.config["SECRET_KEY"] = secret_key
db.init_app(app)
init_db(app)
csrf = CSRFProtect(app)


@login_manager.user_loader
def load_user(user_id):
    # Return the user object from the database based on the user_id
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

        # Check if the user exists in the database based on email
        user = User.query.filter_by(email=email).first()

        if user:
            # Check if the password matches
            if user.check_password(password):
                # Log the user in
                login_user(user)
                flash("Login successful!", "success")
                return redirect(url_for("profile"))  # Redirect to profile page after login
            else:
                flash("Invalid password. Please try again.", "error")
        else:
            flash("User not found. Please check your email and try again.", "error")

    return render_template("login.html", form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print("Form validated successfully!")
        print("Username:", form.username.data)
        print("Email:", form.email.data)
        print("Password:", form.password.data)
        print("Confirm Password:", form.confirm_password.data)
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        
        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('register'))
        
        # Check if email already exists
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('Email already exists. Please use a different one.', 'error')
            return redirect(url_for('register'))
        
        # Insert user into database if all validations pass
        insert_user(username, email, password)
        
        # Automatically sign in the newly registered user
        user = User.query.filter_by(email=email).first()
        login_user(user)
        
        flash('Registration successful! You are now signed in.', 'success')
        return redirect(url_for('profile'))  # Redirect to the profile
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
