import flask
import requests
import bs4
import textblob
from app.results import results
from app.results.sentimenter import Sentimenter

@results.route('/results', methods=('POST',))
def results_page():
    url = flask.request.form.get('url')
    print(url)

    try:
        # fetch page associated with url using requests
        www = requests.get(url)
        if www.status_code != 200:
            raise RuntimeError()
    except:
        # Give error message that this was an invalid url
        flask.flash('Invalid url. Please fix and resubmit.')
        return flask.redirect(flask.url_for('main_page.home_page'))

    # parse results using BeautifulSoup
    souped = bs4.BeautifulSoup(www.content, 'html.parser')
    
    if souped.find('h1'):
        header = souped.find('h1').get_text()
    else:
        header = souped.title.get_text()
    # create TextBlob instance
    blob = textblob.TextBlob(souped.get_text())

    page_results = Sentimenter(www, header, blob)

    return flask.render_template('results.html', page_results=page_results)