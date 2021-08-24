from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from blog.models import User


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField(
        "Password", validators=[DataRequired(), EqualTo("pass_confirm")]
    )
    pass_confirm = PasswordField("Confirm password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def check_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError("Email has been registered already!")

    def check_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError("Username has been taken already!")


class UpdateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    picture = FileField(
        "Upload Profile Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField("Update Profile")

    def check_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError("Email has been registered already!")

    def check_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError("Username has been taken already!")
