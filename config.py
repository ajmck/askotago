import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'defaultsecretkey'

    if os.environ.get('FLASK_ENV') == 'development':
        DEBUG = True
    else:
        print("Environment mode: " + str(os.environ.get('FLASK_MODE')))

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
