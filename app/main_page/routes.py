import flask
import textblob
from app.main_page import main_page

@main_page.route('/')
def home_page():
    test = textblob.TextBlob("Textblob is amazingly simple to use. What great fun!")
    test_score = test.sentiment

    return flask.render_template('main_page.html', test_score = test_score)