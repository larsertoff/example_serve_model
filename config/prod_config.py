import os

FLASK_ENV = 'production'
SECRET_KEY = os.environ.get('SECRET_KEY')