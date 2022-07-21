from flask import Flask
from calsite.config import Config

app = Flask(__name__)

app.config.from_object(Config)


from calsite import routes

