from datetime import datetime, date, timedelta, time
from email.policy import default
from xmlrpc.client import Boolean
from calsite import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

'''The data stored in the databse will be represented by a 
collection of classes, called database models the ORM will
do the translations required to map objects'''

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    events = db.relationship('Events', backref='author',lazy=True)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User {self.fullname}"

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(50))
    invitees = db.Column(db.Text(250), nullable=False)
    # is_cancelled = db.Column(Boolean, unique=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Event {self.title} on {self.start_date} {self.author.fullname}"


