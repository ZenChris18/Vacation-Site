from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, current_user, LoginManager
from models import db, User, init_db
import os

app = Flask(__name__)
secret_key = os.environ.get("SECRET_KEY", "58d3b9a5efb4388ff3c5fd65fe853dcc38b808d739280b06")
app.config["SECRET_KEY"] = secret_key

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
init_db(app)

login_manager = LoginManager(app)
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
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('profile'))
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
            flash("Username already exists!", category="error")
        elif user_by_email:
            flash("Email already exists!", category="error")
        elif len(email) < 4:
            flash("Email is too short!", category="error")
        elif len(username) < 2:
            flash("Username is too short!", category="error")
        elif password != confirm_password:
            flash("Passwords don't match!", category="error")
        elif len(password) < 5:
            flash("Passwords must be greater than 4 characters", category="error")
        else:
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!", category="success")
            return redirect(url_for('login'))
    return render_template("register.html")


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
