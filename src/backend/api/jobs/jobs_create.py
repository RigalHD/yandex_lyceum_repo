from flask import Blueprint, g, jsonify, make_response, request

from backend.db.data.jobs import JobCategories, Jobs
from backend.db.data.users import User

router = Blueprint("api_jobs_create", __name__, url_prefix="/api/jobs")


@router.route("/", methods=["POST"])
# @login_required
def job_create():
    if not request.json:
        return make_response(jsonify({"error": "Empty request"}), 400)
    if not all(
        key in request.json and request.json.get(key) is not None
        for key in ["job", "work_size", "collaborators", "is_finished"]
    ):
        return make_response(jsonify({"error": "Bad request"}), 400)

    db_sess = g.db_session

    job = Jobs(
        job=request.json["job"],
        work_size=request.json["work_size"],
        collaborators=request.json["collaborators"],
        is_finished=request.json["is_finished"],
    )
    job.leader = db_sess.get(User, 1)
    job.category = db_sess.get(JobCategories, 1)
    job.creator = db_sess.get(User, 1)

    db_sess.add(job)
    db_sess.commit()

    return jsonify({"id": job.id})
