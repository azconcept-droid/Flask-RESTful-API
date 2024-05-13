#!myvenv/bin/python3
"""Routes module for the Flask app"""

from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    """Default route, home page"""

    # Mockup for users
    user = {'username': 'Azeez'}

    # Mockup for posts
    posts = [
        {
            'author': {'username': 'James'},
            'body': 'Beautiful day in Lagos'
        },
        {
            'author': {'username': 'Ajoke'},
            'body': 'The Avengers movies was so cool!'
        },
        {
            'author': {'username': 'Usama'},
            'body': 'Quran memo is beautiful'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    """ Login page route """
    form = LoginForm()

    return render_template('login.html', title='Sign In', form=form)
