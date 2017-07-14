import os
from flask import Flask, request, session, redirect, url_for, render_template, flash
import flask_login

from fieri.database import db_session, init_db
from fieri.models import *

init_db()

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

@app.route('/')
def index():
    users = User.query.all()
    print(users)
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == os.environ['PASSWORD']:
            session['logged_in'] = True
            flash('You were successfully logged in!')
        else:
            session['logged_in'] = None
            flash('Wrong password!')
        
        return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session['logged_in'] = None
    flash('Successfully logged out.')
    return redirect(url_for('index'))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()