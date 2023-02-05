from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired


class MainForm(FlaskForm):
    user_search = StringField('user_search', validators=[DataRequired()])
    submit = SubmitField('Search')