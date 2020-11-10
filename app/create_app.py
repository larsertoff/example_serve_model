import flask
import os

def create_app(config_name= 'dev_config.py'):
    '''
    App factory
    '''


    # Initialize app
    app = flask.Flask(__name__)


    
    if os.path.join(os.getcwd(), 'config', config_name):
        app.config.from_pyfile(os.path.join(os.getcwd(), 'config', config_name))
    else:
        app.config.from_pyfile(os.path.join(os.getcwd(), 'config', 'dev_config.py'))
    
    # Import main page blueprint
    from app.main_page import main_page
    app.register_blueprint(main_page)

    # Import results page
    from app.results import results
    app.register_blueprint(results)



    return app
