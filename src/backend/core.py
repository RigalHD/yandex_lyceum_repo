import datetime

from flask import Flask, g, jsonify, make_response, redirect
from flask_login import LoginManager

from backend.db.data import db_session
from backend.db.data.users import User

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "src/backend/static/img"
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(days=365)
app.config["DB_FILE_PATH"] = "src/backend/db/blogs.db"

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id: int) -> User:
    db_sess = g.db_session
    return db_sess.get(User, user_id)


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect("/register")


@app.before_request
def before_request():
    g.db_session = db_session.create_session()


@app.teardown_appcontext
def shutdown_session(exception=None):
    session = g.pop("session", None)
    if session is not None:
        session.close()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({"error": "Bad Request"}), 400)
