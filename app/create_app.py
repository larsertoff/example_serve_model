import flask
import textblob

def create_app(config_name= 'dev_config.py'):



    app = flask.Flask(__name__)

    app.config['SECRET_KEY'] = '123456'
    # I only need one simple route for this for now
    @app.route('/')
    def before_doing_anything():
        test = textblob.TextBlob("Textblob is amazingly simple to use. What great fun!")
        print(test.sentiment)
        return str(test.sentiment)

    return app
