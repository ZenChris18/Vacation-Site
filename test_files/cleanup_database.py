from models import db, User
from app import app

with app.app_context():
    # Find all users with password_hash as None
    users = User.query.filter_by(password_hash=None).all()
    for user in users:
        # Handle the user: either set a new password or delete the user
        user.set_password('defaultpassword')  # You can replace 'defaultpassword' with a more secure password
    db.session.commit()
    print("Cleanup completed!")
