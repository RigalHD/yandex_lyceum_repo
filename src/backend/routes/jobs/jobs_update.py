from typing import Sequence
from flask import Blueprint, g, redirect, render_template
from flask_login import login_required, current_user
from sqlalchemy import select

from backend.db.data.jobs import JobCategories, Jobs
from backend.db.data.users import User
from backend.forms.job import JobForm

router = Blueprint("jobs_update", __name__, url_prefix="/job")


@router.route("/<int:job_id>/update", methods=["GET", "POST"])
@login_required
def job_update(job_id: int):
    db_sess = g.db_session
    job = db_sess.get(Jobs, job_id)

    if job.creator != current_user and current_user.get_id() != 1:
        return render_template("404.html")

    form = JobForm()

    users: Sequence[User] = db_sess.scalars(
        select(User).where(User.id != job.team_leader)
    )

    leader_choice_list: list[User] = [(job.team_leader, job.leader.name)]
    leader_choice_list.extend([(user.id, user.name) for user in users])
    form.team_leader.choices = leader_choice_list

    job_categories: Sequence[JobCategories] = db_sess.scalars(
        select(JobCategories).where(JobCategories.id != job.category.id)
    )
    category_choice_list: list[JobCategories] = [
        (job.category.id, f"{job.category.id}. {job.category.name}")
    ]
    category_choice_list.extend(
        [
            (category.id, f"{category.id}. {category.name}")
            for category in job_categories
        ]
    )
    form.category.choices = category_choice_list

    if form.validate_on_submit():
        job.leader = db_sess.get(User, form.team_leader.data)
        job.category = db_sess.get(JobCategories, form.category.data)

        job.job = form.job.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = form.is_finished.data

        db_sess.merge(job)
        db_sess.commit()

        return redirect("/")

    form.job.data = job.job
    form.work_size.data = job.work_size
    form.collaborators.data = job.collaborators
    form.is_finished.data = job.is_finished

    return render_template(
        "jobs_create.html", title="Редактирование работы", form=form, edit_mode=True
    )
