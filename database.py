import sqlite3
from models import db


def init_db(app):
    with app.app_context():
        db.create_all()

def insert_user(username, email, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
    conn.commit()
    conn.close()
