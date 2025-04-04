from typing import Sequence
from flask import Blueprint, g, jsonify, make_response
from flask_login import login_required
from sqlalchemy import select

from backend.db.data.jobs import Jobs

router = Blueprint("api_jobs_retrieve", __name__, url_prefix="/api/jobs")


@router.route("/")
@login_required
def jobs_retrieve():
    db_sess = g.db_session
    jobs: Sequence[Jobs] = db_sess.scalars(select(Jobs))

    json_response = {"jobs": [job.to_dict() for job in jobs]}

    return jsonify(json_response)


@router.route("/<int:job_id>")
@login_required
def job_retrieve(job_id: int):
    db_sess = g.db_session
    job: Jobs = db_sess.get(Jobs, job_id)
    if job is None:
        return make_response(jsonify({"error": "Not found"}), 404)
    json_response = job.to_dict()
    return jsonify(json_response)
