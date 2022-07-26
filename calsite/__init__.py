from flask import Flask
from calsite.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


login = LoginManager(app)
login.login_view = 'login'


from calsite import routes, models
# models will define the structure of the database


#db.create_all()