import click

from app.extensions import db
from app.models import Course, Mentor

def init_db():
    db.drop_all()
    db.create_all()

def populate_db():
    mentor = Mentor(name="prof1", about="prof info", photo="poto")
    db.session.add(mentor)
    db.session.commit()

    courses = [
        {"id": 1, "title": "course 1", "description": "description 1",
         "syllabus_link": "link1", "type": "course", "registration_link": "link1", "mentor_id": 1},
        {"id": 2, "title": "course 2", "description": "description 2",
         "syllabus_link": "link2", "type": "course", "registration_link": "link2", "mentor_id": 1}
    ]

    for course in courses:
        new_course = Course(title=course["title"], description=course["description"],
                             syllabus_link=course["syllabus_link"], type=course["type"],
                            registration_link=course["registration_link"], mentor_id=course["mentor_id"])
        db.session.add(new_course)
    db.session.commit()

@click.command('init_db')
def init_db_command():
    init_db()
    click.echo('Database initialized!')

@click.command('populate_db')
def populate_db_command():
    populate_db()