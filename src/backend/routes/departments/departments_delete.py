from flask import Blueprint, g, redirect, render_template
from flask_login import login_required, current_user

from backend.db.data.departments import Department

router = Blueprint("departments_delete", __name__, url_prefix="/department")


@router.route("/<int:department_id>/delete", methods=["GET", "POST"])
@login_required
def department_delete(department_id: int):
    db_sess = g.db_session
    department = db_sess.get(Department, department_id)

    if department.department_chief != current_user and current_user.get_id() != 1:
        return render_template("404.html")

    db_sess.delete(department)
    db_sess.commit()
    db_sess.close()
    return redirect("/departments")
