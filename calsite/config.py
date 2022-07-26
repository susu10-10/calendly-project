import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'cal.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


'''using seperation of concerns to keep our configuration key in another module
the flask-sqlalc takes the locatin of the app database also
with a fall back variable incase no enviromen variable was configured
cal.db will be located in the main directory of our application 
which is stored in the basedir variable
'''