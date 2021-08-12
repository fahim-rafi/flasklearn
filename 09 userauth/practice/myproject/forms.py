from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from myproject.models import User

class LoginForm(FlaskForm):
    email = StringField('Email:&#160', validators=[DataRequired(), Email()])
    password = PasswordField('Password:&#160', validators=[DataRequired()])
    submit = SubmitField("Log In!")

class RegistrationForm(FlaskForm):
    email = StringField('Email:&#160', validators=[DataRequired(), Email()])
    username = StringField('Username:&#160', validators=[DataRequired()])
    password = PasswordField('Password:&#160', validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm password:&#160', validators=[DataRequired()])
    submit = SubmitField("Register!")

    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has been registered already!')
    
    def validate_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username has been taken already!')
