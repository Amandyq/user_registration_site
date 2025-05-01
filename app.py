from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Дерекқорды бастапқы жасау
def init_db():
    if not os.path.exists("users.db"):
        conn = sqlite3.connect('users.db')
        conn.execute('''CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )''')
        conn.close()

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    try:
        conn.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                     (name, email, password))
        conn.commit()
        message = "Тіркелу сәтті аяқталды!"
    except sqlite3.IntegrityError:
        message = "Мұндай email бұрын тіркелген."
    finally:
        conn.close()
    
    return message

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
