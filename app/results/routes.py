import flask
from app.results import results
import requests

@results.route('/results', methods=('GET','POST'))
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

    # create TextBlob instance

    # process TextBlob text analytics results

    return flask.render_template('results.html', page_results={})