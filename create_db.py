import sqlite3
from werkzeug.security import generate_password_hash

def create_db():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()

    # Ajouter un utilisateur admin
    cursor.execute('''
        INSERT INTO users (username, password) VALUES (?, ?)
    ''', ('admin', generate_password_hash('admin123')))  # Modifier si besoin
    conn.commit()

    conn.close()

create_db()
