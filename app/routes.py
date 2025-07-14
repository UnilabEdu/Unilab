from flask import Blueprint, jsonify
from .extensions import db
from .models import User

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return jsonify(message="Hello, Flask + SQLAlchemy!"), 200