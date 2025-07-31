from flask import Flask


def create_app(config_class='config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):
    from .extensions import db
    db.init_app(app)


def register_blueprints(app):
    from .api.hello import bp
    app.register_blueprint(bp, url_prefix='/api')


def register_commands(app):
    from .commands import init_db_command
    app.cli.add_command(init_db_command)


# Add this import to ensure models are registered
from app.models import User, Mentor, Course