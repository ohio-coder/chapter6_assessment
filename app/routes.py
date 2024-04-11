from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    """Index URL"""
    return render_template('index.html' , title="index page")

@app.route('/about-me')
def about_me():
    """About me URL"""
    return render_template('about_me.html' , title="About me page")


