from typing import Sequence
from flask import Blueprint, g, redirect, render_template
from flask_login import login_required, current_user
from sqlalchemy import select

from backend.db.data.jobs import JobCategories, Jobs
from backend.db.data.users import User
from backend.forms.job import JobForm

router = Blueprint("jobs_create", __name__, url_prefix="/job")


@router.route("/create", methods=["GET", "POST"])
@login_required
def job_create():
    form = JobForm()
    db_sess = g.db_session

    users: Sequence[User] = db_sess.scalars(select(User))
    form.team_leader.choices = [(user.id, user.name) for user in users]

    job_categories: Sequence[JobCategories] = db_sess.scalars(select(JobCategories))
    form.category.choices = [
        (category.id, f"{category.id}. {category.name}") for category in job_categories
    ]

    if form.validate_on_submit():
        job = Jobs(
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data,
        )

        job.leader = db_sess.get(User, form.team_leader.data)
        job.category = db_sess.get(JobCategories, form.category.data)
        job.creator = db_sess.get(User, current_user.get_id())

        db_sess.add(job)
        db_sess.commit()

        return redirect("/")

    return render_template("jobs_create.html", title="Добавление работы", form=form)
