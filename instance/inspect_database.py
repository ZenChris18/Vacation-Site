import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Query to get all users
cursor.execute("SELECT id, username, email, password_hash FROM user")
users = cursor.fetchall()

# Print user data
for user in users:
    print(user)

# Close the connection
conn.close()
