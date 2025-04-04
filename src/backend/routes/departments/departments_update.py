from flask import Blueprint, g, redirect, render_template
from flask_login import login_required, current_user
from sqlalchemy import select

from backend.db.data.departments import Department
from backend.db.data.users import User
from backend.forms.department import DepartmentForm

router = Blueprint("departments_update", __name__, url_prefix="/department")


@router.route("/<int:department_id>/update", methods=["GET", "POST"])
@login_required
def department_update(department_id: int):
    db_sess = g.db_session
    department = db_sess.get(Department, department_id)

    if department.department_chief != current_user and current_user.get_id() != 1:
        return render_template("404.html")

    form = DepartmentForm()

    users = db_sess.scalars(select(User).where(User.id != department.chief_id))

    choice_list: list[User] = [(department.chief_id, department.department_chief.name)]

    choice_list.extend([(user.id, user.name) for user in users])

    form.department_chief.choices = choice_list

    if form.validate_on_submit():
        department.department_chief = db_sess.get(User, form.department_chief.data)

        department.title = form.title.data
        department.members = form.members.data
        department.email = form.email.data

        db_sess.merge(department)
        db_sess.commit()
        db_sess.close()

        return redirect("/departments")

    form.title.data = department.title
    form.members.data = department.members
    form.email.data = department.email

    return render_template(
        "departments_create.html",
        title="Редактирование департамента",
        form=form,
        edit_mode=True,
    )
