import flask

def create_app(config_name= 'dev_config.py'):



    app = flask.Flask(__name__)

    app.config['SECRET_KEY'] = '123456'
    # Split this out as blueprints if needed
    @app.route('/')
    def before_doing_anything():
        return 'Before doing anything'

    return app
