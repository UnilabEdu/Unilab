import click
from app.extensions import db

@click.command('init-db')
def init_db_command():
    """Create database tables"""
    db.create_all()
    click.echo('Database initialized!')