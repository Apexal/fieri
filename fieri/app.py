import os
from flask import Flask, request, session, redirect, url_for, render_template, flash
import flask_login

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #session['username'] = request.form['username']
        return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    
    return 'Logged out'