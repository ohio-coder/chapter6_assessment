from app import app
from flask import render_template

@app.route('/')
@app.route('/shop')
def home():
    """Shop URL"""
    return render_template('shop.html' , title="shop page")

@app.route('/register')
def register():
    """Register URL"""
    return render_template('register.html' , title="register page")
@app.route('/login')
def login():
    """Login URL"""
    return render_template('login.html' , title="login page")





