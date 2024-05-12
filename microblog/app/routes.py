#!myvenv/bin/python3
"""Routes module for the Flask app"""

from app import app

@app.route('/')
@app.route('/index')
def index():
    """Default route, home page"""

    user = {'username': 'Azeez'}

    return '''
<html>
    <head>
        <title>Home page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>
'''
