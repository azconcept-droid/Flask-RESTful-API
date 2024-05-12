#!myvenv/bin/python3
"""Routes module for the Flask app"""

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    """Default route, home page"""

    user = {'username': 'Azeez'}

    return render_template('index.html', title='Home', user=user)
