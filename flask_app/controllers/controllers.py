from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.model import Email


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop')
def store():
    return render_template('shop.html')

@app.route('/select')
def create():
    return render_template('class_selection.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')