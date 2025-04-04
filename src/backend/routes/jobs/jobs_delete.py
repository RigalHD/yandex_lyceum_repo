from flask import Blueprint, g, redirect, render_template
from flask_login import login_required, current_user

from backend.db.data.jobs import Jobs

router = Blueprint("jobs_delete", __name__, url_prefix="/job")


@router.route("/<int:job_id>/delete", methods=["GET", "POST"])
@login_required
def job_delete(job_id: int):
    db_sess = g.db_session
    job = db_sess.get(Jobs, job_id)

    if job.creator != current_user and current_user.get_id() != 1:
        return render_template("404.html")

    db_sess.delete(job)
    db_sess.commit()

    return redirect("/")
