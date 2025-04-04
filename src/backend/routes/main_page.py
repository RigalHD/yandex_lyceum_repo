from typing import Sequence
from flask import Blueprint, g, render_template
from flask_login import login_required
from sqlalchemy import select

from backend.db.data.jobs import Jobs

router = Blueprint("main_page", __name__)


@router.route("/")
@login_required
def index():
    db_sess = g.db_session
    jobs: Sequence[Jobs] = db_sess.scalars(select(Jobs))
    return render_template("index.html", jobs=jobs)
