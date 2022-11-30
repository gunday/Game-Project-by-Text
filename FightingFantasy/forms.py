from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired



class HeroStats(Form):
    hstam = StringField('Stamina:', validators=[DataRequired()])
    hskill = StringField('Skill:', validators=[DataRequired()])
    hluck = StringField('Luck:', validators=[DataRequired()])
    estam = StringField('Stamina:', validators=[DataRequired()])
    eskill = StringField('Skill:', validators=[DataRequired()])


class LoginForm(Form):
    username = StringField('Your Username:', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
