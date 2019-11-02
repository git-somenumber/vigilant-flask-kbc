from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class playGame(FlaskForm):
    startGame = SubmitField('Start Game')


class Game(FlaskForm):
    answer = StringField('Gimme the answer', validators=[DataRequired()])
    submit = SubmitField('Lock the answer')