import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'



'''using seperation of concerns to keep our configuration key in another module
'''