from flask import Blueprint, g, redirect, render_template
from flask_login import login_required, current_user

from backend.db.data.jobs import JobCategories
from backend.forms.job import JobCategoryForm

router = Blueprint("job_categories_create", __name__, url_prefix="/job/category")


@router.route("/create", methods=["GET", "POST"])
@login_required
def job_category_create():
    if current_user.get_id() != 1:  # Категорию может создать только капитан
        return render_template("404.html")

    form = JobCategoryForm()

    if form.validate_on_submit():
        db_sess = g.db_session
        job_category = JobCategories(name=form.name.data)

        db_sess.add(job_category)
        db_sess.commit()

        return redirect("/")

    return render_template(
        "job_categories_create.html", title="Добавление категории", form=form
    )
