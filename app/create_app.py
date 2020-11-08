import flask
import textblob

def create_app(config_name= 'dev_config.py'):
    '''
    App factory
    '''


    # Initialize app
    app = flask.Flask(__name__)

    # Make config proper here
    app.config['SECRET_KEY'] = '123456'
    

    # Import main page blueprint
    from app.main_page import main_page
    app.register_blueprint(main_page)
    
    return app
