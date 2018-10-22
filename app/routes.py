from flask import render_template
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Chris'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Something John would say.'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Some other title.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)