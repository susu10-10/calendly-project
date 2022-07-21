from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Enter your email to get started.', 
                        validators=[DataRequired(), Email()]
                        )
    fullname = StringField('Enter your full name',
                            validators=[DataRequired()]
                            )
    password = PasswordField('Choose a password with aleast 8 characters.', validators=[DataRequired(), Length(min=8)])
    confim_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, username):
        # check if user submitted is already
        pass

class LoginForm(FlaskForm):
    email = StringField('email', 
                        validators=[DataRequired(), Email()]
                        )

    password = PasswordField('Enter your password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Continue')