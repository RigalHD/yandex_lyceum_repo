from argparse import ArgumentParser

from backend.api.users.users_resource import UserResource, UsersResource
from backend.core import api
from backend.core import app
from backend.db.data import db_session
from backend.misc.router_register import register_routers
from backend.routes import routers as app_routers
from backend.api import routers as api_routers


def main():
    parser = ArgumentParser()

    parser.add_argument("--drop-db", type=str, default="False")
    args = parser.parse_args()

    db_file_path = app.config["DB_FILE_PATH"]
    drop_db = True if args.drop_db.lower() == "true" else False

    db_session.global_init(db_file=db_file_path, drop_db=drop_db)

    routers = (*app_routers, *api_routers)

    register_routers(routers)
    api.add_resource(UsersResource, "/api/users")
    api.add_resource(UserResource, "/api/users/<int:user_id>")
    app.run()


if __name__ == "__main__":
    main()
