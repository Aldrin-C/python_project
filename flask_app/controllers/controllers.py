from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.model import Email


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process/login', methods=['post'])
def login():
    return redirect ('/dashboard')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/select')
def create():
    return render_template('class_selection.html')

# ---- Dashboard ----
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# ---- Account ----
@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/account/update', methods=['post'])
def account_update():
    return redirect ('/account')

# ---- Farm ----
@app.route('/farm')
def farm():
    return render_template('farm.html')

# ---- Dojo ----
@app.route('/dojo')
def dojo():
    return render_template('dojo.html')