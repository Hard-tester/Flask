from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "<p>login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def signup():
    return "<p>sign-up</p>"

@auth.route('/sign-in')
def signin():
    return "<p>sign-in</p>"