from app.models.base import BaseModel
from app.extensions import db

class Course(BaseModel):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    syllabus_link = db.Column(db.String(255), nullable=True)
    type = db.Column(db.String(100), nullable=False)
    registration_link = db.Column(db.String(255), nullable=False)

    mentor_id = db.Column(db.Integer, db.ForeignKey('mentors.id'))
    mentor = db.relationship("Mentor", back_populates="courses")

    def __str__(self):
        return self.title