from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return "<h1>Index<h1>"

@views.route('/characters')
def characters():
    return "<h1>Characters<h1>"

@views.route('/races')
def races():
    return "<h1>Races<h1>"

@views.route('/classes')
def classes():
    return "<h1>Classes<h1>"

@views.route('/backgrounds')
def backgrounds():
    return "<h1>Backgrounds<h1>"