from flask import Flask, jsonify, request, render_template
import sqlite3
import hashlib

app = Flask(__name__)


def validate(username, password):
    con = sqlite3.connect('database.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        for row in rows:
            dbUser = row[1]
            dbPass = row[2]
            if dbUser == username and dbPass==password:
                return True
    return False


@app.route('/')
def home():
    return render_template('login_page.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['email-address']
        password = request.form['password']
        completion = validate(username, password)
        if not completion:
            error = "Invalid credentials"
        else:
            return render_template('login_page.html', error=error)


app.run(port=5000)
