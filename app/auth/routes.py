from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect("/admin")
        else:
            flash("დაფიქსირდა შეცდომა!", "error")

    return render_template("login.html")


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect('/')