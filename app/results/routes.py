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
        print(www)    
    except:
        # Give error message that this was an invalid url
        pass

    # parse results using BeautifulSoup

    # create TextBlob instance

    # process TextBlob text analytics results

    return flask.render_template('results.html', page_results={})