from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
                    SubmitField, DateField, TimeField,
                    TextAreaField, DateTimeField)
from wtforms.validators import DataRequired,ValidationError
from calsite.models import User


class RegistrationForm(FlaskForm):
    email = StringField('Enter your email to get started.', 
                        validators=[DataRequired()])
    fullname = StringField('Enter your full name',
                            validators=[DataRequired()])
    password = PasswordField('Choose a password with aleast 8 characters.', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        # check if user submitted is already
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already Taken')



class LoginForm(FlaskForm):
    password = PasswordField('Enter your password', validators=[DataRequired()])
    submit = SubmitField('Continue')


class EmailForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired()])
    submit = SubmitField('Log in')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            return user
        else:
            raise ValidationError('Email not found')


class EventForm(FlaskForm):
    title = StringField('Enter the title of your Event')
    start_date = DateField('Enter Start Date',validators=[DataRequired()], id='datepick')
    end_date = DateField('Enter end date',validators=[DataRequired()], id='datepick')
    start_time = TimeField('Time Start')
    end_time = TimeField('Time End')
    description = TextAreaField('Description', validators=[DataRequired()])
    invitees = TextAreaField('Participants(separted by comma)', validators=[DataRequired()])
    submit = SubmitField('Continue')