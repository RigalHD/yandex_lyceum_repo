from flask import Blueprint, g, redirect, render_template
from flask_login import login_required, current_user

from backend.db.data.jobs import JobCategories
from backend.forms.job import JobCategoryForm

router = Blueprint("jobs_categories_update", __name__, url_prefix="/job/category/")


@router.route("/<int:job_category_id>/update", methods=["GET", "POST"])
@login_required
def job_category_update(job_category_id: int):
    if current_user.get_id() != 1:  # Категорию может обновить только капитан
        return render_template("404.html")

    db_sess = g.db_session
    job_category = db_sess.get(JobCategories, job_category_id)

    form = JobCategoryForm()

    if form.validate_on_submit():
        job_category.name = form.name.data

        db_sess.merge(job_category)
        db_sess.commit()

        return redirect("/")

    form.name.data = job_category.name

    return render_template(
        "job_categories_create.html",
        title="Редактирование категории",
        form=form,
        edit_mode=True,
    )
