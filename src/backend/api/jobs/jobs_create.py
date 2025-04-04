from typing import Sequence
from flask import Blueprint, g, jsonify, make_response, request
from flask_login import login_required
from sqlalchemy import select

from backend.db.data.jobs import Jobs

router = Blueprint("api_jobs_create", __name__, url_prefix="/api/jobs")


@router.route("/", methods=["POST"])
@login_required
def job_create():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    if not all(key in request.json for key in ["job", "work_size", "collaborators", "is_finished"]):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    
    db_sess = g.db_session

    job = Jobs(
        job=request.json["job"],
        work_size=request.json["work_size"],
        collaborators=request.json["collaborators"],
        is_finished=request.json["is_finished"],
    )

    db_sess.add(job)
    db_sess.commit()

    return jsonify({'id': job.id})