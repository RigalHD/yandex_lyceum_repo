from flask import Blueprint

from backend.core import app


def register_routers(routers: tuple[Blueprint]) -> None:
    for router in routers:
        app.register_blueprint(router)
