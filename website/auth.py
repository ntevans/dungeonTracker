from flask import Blueprint

auth = Blueprint('auth', __name__)

# User login page
@auth.route('/login')
def login():
    return "<h1>Login<h1>"

# User sign up page
@auth.route('/sign-up')
def signup():
    return "<h1>Sign Up<h1>"

# User logout function
@auth.route('/logout')
def logout():
    return "<h1>Logout<h1>"