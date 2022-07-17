from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    email = StringField('Enter your email to get started.', 
                        validators=[DataRequired(), Email()]
                        )
    fullname = StringField('Enter your full name',
                            validators=[DataRequired(), Length(min=2, max=20)]
                            )

    password = PasswordField('Choose a password with aleast 8 characters.', validators=[DataRequired(), Length(min=8)])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('email', 
                        validators=[DataRequired(), Email()]
                        )

    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')