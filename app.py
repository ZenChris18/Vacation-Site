from flask import Flask, render_template, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from forms import LoginForm, RegisterForm
import os


secret_key = os.environ.get("SECRET_KEY", "58d3b9a5efb4388ff3c5fd65fe853dcc38b808d739280b06")
app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key
csrf = CSRFProtect(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        return redirect(url_for("home"))
    return render_template("login.html", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/saved")
def saved():
    return render_template("saved.html")

if __name__ == "__main__":
    app.run(debug=True)
