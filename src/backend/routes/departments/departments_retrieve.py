from typing import Sequence
from flask import Blueprint, g, render_template
from flask_login import login_required
from sqlalchemy import select

from backend.db.data.departments import Department

router = Blueprint("departments_retrieve", __name__)


@router.route("/departments")
@login_required
def departments_retieve():
    db_sess = g.db_session
    departments: Sequence[Department] = db_sess.scalars(select(Department))

    return render_template("departments_retrieve.html", departments=departments)
