from flask import Blueprint

views = Blueprint('views', __name__)

# Home page
@views.route('/')
def index():
    return "<h1>Index<h1>"

# Where users manage character sheets
@views.route('/characters')
def characters():
    return "<h1>Characters<h1>"

# Information regarding various races
@views.route('/races')
def races():
    return "<h1>Races<h1>"

# Information regarding various classes
@views.route('/classes')
def classes():
    return "<h1>Classes<h1>"

# Information regarding various backgrounds
@views.route('/backgrounds')
def backgrounds():
    return "<h1>Backgrounds<h1>"