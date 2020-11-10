import flask
import os
import pyodbc

def create_app(config_name= 'dev_config.py'):
    '''
    App factory
    '''

    # Initialize app
    app = flask.Flask(__name__)

    # Options for config can be done in many ways
    if os.path.join(os.getcwd(), 'config', config_name):
        app.config.from_pyfile(os.path.join(os.getcwd(), 'config', config_name))
    else:
        app.config.from_pyfile(os.path.join(os.getcwd(), 'config', 'dev_config.py'))
    
    # To get the SECRET_KEY when deployed
    if os.environ.get('SECRET_KEY') is not None: 
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    if os.environ.get('CONNECTION_STRING') is not None: 
        app.config['CONNECTION_STRING'] = os.environ.get('CONNECTION_STRING')
    
    con_str = app.config['CONNECTION_STRING']
    print(con_str)
    con = pyodbc.connect(con_str)

    # Import main page blueprint
    from app.main_page import main_page
    app.register_blueprint(main_page)

    # Import results page
    from app.results import results
    app.register_blueprint(results)

    return app
