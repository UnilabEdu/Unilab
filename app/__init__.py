from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt, mail
from .routes import bp as main_bp
from .cli import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)

    app.register_blueprint(main_bp)
    app.cli.add_command(init_db)

    return app