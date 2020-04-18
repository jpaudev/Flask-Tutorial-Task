from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jaka'}
    posts = [
        {
            'author': {'username': 'Samantha'},
            'body': 'Everyday is a good day!'
        },
        {
            'author': {'username': 'Rhea'},
            'body': 'Programming is really interesting!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)