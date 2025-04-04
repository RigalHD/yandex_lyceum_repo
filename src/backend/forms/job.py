from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    BooleanField,
    IntegerField,
    SelectField,
)
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    job = StringField("Название работы", validators=[DataRequired()])
    work_size = IntegerField("Время работы (в часах)", validators=[DataRequired()])
    team_leader = SelectField("Лидер команды", validators=[DataRequired()])
    collaborators = StringField("Участники работы", validators=[DataRequired()])
    category = SelectField("Категория", validators=[DataRequired()])
    is_finished = BooleanField("Работа уже завершена?")

    submit = SubmitField("Добавить работу")


class JobCategoryForm(FlaskForm):
    name = StringField("Название категории", validators=[DataRequired()])

    submit = SubmitField("Добавить категорию")
