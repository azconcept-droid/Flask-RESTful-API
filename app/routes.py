#!myvenv/bin/python3
"""Routes module for the Flask app"""

from app import app

@app.route('/')
@app.route('/index')
def index():
    """Default route, home page"""
    return "Hello, World!"
