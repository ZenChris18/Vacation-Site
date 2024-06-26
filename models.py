from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method="pbkdf2:sha256")

    def check_password(self, password):
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)

    def update_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.set_password(new_password)
            return True
        return False

    @property
    def is_active(self):
        # Return True if the user is active, False otherwise
        return True 

class SavedSpot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spot_name = db.Column(db.String(200), nullable=False)
    spot_location = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def init_db(app):
    with app.app_context():
        db.create_all()
