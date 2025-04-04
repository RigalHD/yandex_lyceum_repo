from flask_wtf import FlaskForm
from wtforms import (
    EmailField,
    StringField,
    SubmitField,
    SelectField,
)
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    title = StringField("Название департамента", validators=[DataRequired()])
    department_chief = SelectField("Лидер департамента", validators=[DataRequired()])
    members = StringField("Работники департамента", validators=[DataRequired()])
    email = EmailField("Почта", validators=[DataRequired()])

    submit = SubmitField("Добавить департамент")
