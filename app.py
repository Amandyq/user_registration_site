from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Дерекқорды алғаш рет жасау
def init_db():
    conn = sqlite3.connect('users.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)')
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
    conn.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, password))
    conn.commit()
    conn.close()
    return redirect('/success')

@app.route('/success')
def success():
    return "Тіркелу сәтті аяқталды!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
