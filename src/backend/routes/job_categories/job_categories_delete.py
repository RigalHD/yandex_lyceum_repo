from flask import Blueprint, g, redirect, render_template
from flask_login import login_required, current_user

from backend.db.data.jobs import JobCategories

router = Blueprint("jobs_categories_delete", __name__, url_prefix="/job/category/")


@router.route("/<int:job_category_id>/delete", methods=["GET", "POST"])
@login_required
def job_category_delete(job_category_id: int):
    if current_user.get_id() != 1:  # Категорию может удалить только капитан
        return render_template("404.html")

    db_sess = g.db_session
    job_category = db_sess.get(JobCategories, job_category_id)

    db_sess.delete(job_category)
    db_sess.commit()

    return redirect("/")
