from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    due_date = DateField('due_date', validators=[DataRequired()])
    priority = IntegerField('priority', validators=[DataRequired()])
    completed = SelectField('Completed', choices=[("False", "False"), ("True", "True")], validators=[DataRequired()])
    submit = SubmitField("Submit")
