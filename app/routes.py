from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'ismail'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Dubai!'
        },
        {
            'author': {'username': 'Ibrahim'},
            'body': 'Wonderful day!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
