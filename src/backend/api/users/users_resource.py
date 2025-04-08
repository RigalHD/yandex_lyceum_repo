from typing import Sequence
from flask import Response, g, jsonify, make_response
from flask_restful import Resource
from sqlalchemy import select, exc
from sqlalchemy.orm import Session
from flask_restful.reqparse import RequestParser

from backend.db.data.users import User
from backend.misc.abort import abort_if_not_found


class UsersResource(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.user_parser = RequestParser()
        self._set_user_parser()

    def _set_user_parser(self) -> None:
        self.user_parser.add_argument("surname", required=True)
        self.user_parser.add_argument("name", required=True)
        self.user_parser.add_argument("age")
        self.user_parser.add_argument("position")
        self.user_parser.add_argument("speciality")
        self.user_parser.add_argument("address")
        self.user_parser.add_argument("email", required=True)
        self.user_parser.add_argument("password", required=True)

    def get(self) -> Response:
        db_session: Session = g.db_session
        users: Sequence[User] = db_session.scalars(select(User))
        return jsonify({"users": [user.to_dict() for user in users]})

    def post(self) -> Response:
        parser_args = self.user_parser.parse_args()
        db_session: Session = g.db_session
        try:
            user = User(
                surname=parser_args["surname"],
                name=parser_args["name"],
                age=parser_args.get("age"),
                position=parser_args.get("position"),
                speciality=parser_args.get("speciality"),
                address=parser_args.get("address"),
                email=parser_args["email"],
            )
        except:
            return make_response(jsonify({"error": "Bad request"}), 400)
        user.set_password(parser_args["password"])
        db_session.add(user)
        try:
            db_session.commit()
        except exc.IntegrityError:
            return make_response(jsonify({"error": "Such email is already used"}), 400)
        return jsonify({"id": user.id})


class UserResource(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.user_parser = RequestParser()
        self._set_user_parser()

    def _set_user_parser(self) -> None:
        self.user_parser.add_argument("surname")
        self.user_parser.add_argument("name")
        self.user_parser.add_argument("age")
        self.user_parser.add_argument("position")
        self.user_parser.add_argument("speciality")
        self.user_parser.add_argument("address")
        self.user_parser.add_argument("email")
        self.user_parser.add_argument("password")

    def get(self, user_id: int) -> Response:
        abort_if_not_found(User, user_id)
        db_session: Session = g.db_session
        user: User = db_session.get(User, user_id)

        return jsonify({"user": user.to_dict()})

    def put(self, user_id: int) -> Response:
        parser_args = self.user_parser.parse_args()

        if len(parser_args.keys()) == 0:
            return make_response(jsonify({"error": "Bad request"}), 400)

        db_session: Session = g.db_session
        user = db_session.get(User, user_id)

        user.surname = parser_args.get("surname") or user.surname
        user.name = parser_args.get("name") or user.name
        user.age = parser_args.get("age") or user.age
        user.position = parser_args.get("position") or user.position
        user.speciality = parser_args.get("speciality") or user.speciality
        user.address = parser_args.get("address") or user.address
        user.email = parser_args.get("email") or user.email

        if parser_args.get("password"):
            user.set_password(parser_args.get("password"))

        db_session.merge(user)
        try:
            db_session.commit()
        except exc.IntegrityError:
            return make_response(jsonify({"error": "Such email is already used"}), 400)
        return jsonify({"id": user.id})

    def delete(self, user_id: int) -> Response:
        abort_if_not_found(User, user_id)
        db_session: Session = g.db_session
        user = db_session.get(User, user_id)
        db_session.delete(user)
        db_session.commit()
        return jsonify({"message": f"User with id={user_id} was fired"})
