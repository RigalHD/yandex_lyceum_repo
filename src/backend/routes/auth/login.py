from flask import Blueprint, g, redirect, render_template, session
from flask_login import login_required, login_user, logout_user

from backend.db.data.users import User
from backend.forms.auth import LoginForm

router = Blueprint("login", __name__)


@router.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    session.pop("username", None)
    return redirect("/register")


@router.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = g.db_session
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            session["username"] = f"{user.name} {user.surname}"
            session["user_id"] = user.id
            return redirect("/")

        return render_template(
            "login.html", message="Неправильный логин или пароль", form=form
        )
    return render_template("login.html", title="Авторизация", form=form)
