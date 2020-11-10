import flask

results = flask.Blueprint('results', __name__, template_folder='templates')

from app.results import routes