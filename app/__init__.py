from flask import Flask
from app.config import Config
from .commands import populate_db_command, init_db_command
from .extensions import db, migrate, api
from app.endpoints import CourseApi

COMMANDS = [init_db_command, populate_db_command]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_commands(app)

    return app


def register_extensions(app):
    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    # Flask-Restx
    api.init_app(app)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


# Add this import to ensure models are registered
from app.models import User, Mentor, Course, News