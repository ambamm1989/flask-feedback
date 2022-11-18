from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=1, max=20)],)
    password = PasswordField(validators=[InputRequired(), Length(min=6, max=55)],)

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=1, max=20)],)
    password = PasswordField(validators=[InputRequired(), Length(min=6, max=55)],)
    email = StringField(validators=[InputRequired(), Email(), Length(max=50)],)
    first_name = StringField( validators=[InputRequired(), Length(max=30)],)
    last_name = StringField(validators=[InputRequired(), Length(max=30)],)

class FeedbackForm(FlaskForm):
    title = StringField(validators=[InputRequired(), Length(max=100)],)
    content = StringField(validators=[InputRequired()],)

class DeleteForm(FlaskForm):
    