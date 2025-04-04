from typing import Sequence
from flask import Blueprint, g, redirect, render_template
from flask_login import login_required
from sqlalchemy import select

from backend.db.data.departments import Department
from backend.db.data.users import User
from backend.forms.department import DepartmentForm

router = Blueprint("departments_create", __name__, url_prefix="/department")


@router.route("/create", methods=["GET", "POST"])
@login_required
def department_create():
    form = DepartmentForm()
    db_sess = g.db_session
    users: Sequence[User] = db_sess.scalars(select(User))
    form.department_chief.choices = [(user.id, user.name) for user in users]
    if form.validate_on_submit():
        department = Department(
            title=form.title.data,
            members=form.members.data,
            email=form.email.data,
        )

        department.department_chief = db_sess.get(User, form.department_chief.data)

        db_sess.add(department)
        db_sess.commit()
        db_sess.close()
        return redirect("/departments")

    return render_template(
        "departments_create.html", title="Добавление департамента", form=form
    )
