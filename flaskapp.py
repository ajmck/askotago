from app import app
import os

app = Flask(__name__)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'defaultsecretkey'

    if os.environ.get('FLASK_ENV') == 'development':
        print("Development mode set in environment")
        environment = 'development'
        DEBUG = True
    else:
        print("Environment mode: " + str(os.environ.get('FLASK_MODE')))
