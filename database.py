from models import db, User

def init_db(app):
    with app.app_context():
        db.create_all()

def insert_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)  # Hash the password before storing it
    db.session.add(user)
    db.session.commit()
