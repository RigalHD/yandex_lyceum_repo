from typing import TypeVar
from flask import g
from flask_restful import abort

from backend.db.data.base import BaseModel

db_object = TypeVar("db_object", bound=BaseModel)


def abort_if_not_found(obj_type: db_object, obj_id: int):
    session = g.db_session
    objects = session.get(obj_type, obj_id)
    if not objects:
        abort(404, message=f"{obj_type.__class__.__name__} {obj_id} not found")
