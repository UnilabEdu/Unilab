from app.models.base import BaseModel
from app.extensions import db

class Course(BaseModel):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    syllabus_link = db.Column(db.String(255), nullable=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('mentors.id'), nullable=False)