from flask import Flask
from flask_admin.menu import MenuLink

from app.config import Config
from .commands import populate_db_command, init_db_command
from .extensions import db, migrate, api, login_manager, admin
from app.endpoints import CourseApi, NewsApi
from app.admin_views.base import SecureIndexView
from app.admin_views import CourseView, MentorView, NewsView, SliderView, ProjectView
from app.auth.routes import auth_bp

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

    # Flask-Login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)

    # Flask-Admin
    admin.init_app(app, index_view=SecureIndexView())
    admin.add_view(CourseView(Course, db.session))
    admin.add_view(MentorView(Mentor, db.session))
    admin.add_view(NewsView(News, db.session))
    admin.add_view(SliderView(Slider, db.session))
    admin.add_view(ProjectView(Project, db.session))

    admin.add_link(MenuLink("Log Out", url="/logout", icon_type="fa", icon_value="fa-sign-out"))

    # Blueprint
    app.register_blueprint(auth_bp)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


# Add this import to ensure models are registered
from app.models import User, Mentor, Course, News, Slider, Project, ProjectUser