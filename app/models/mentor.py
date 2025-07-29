from app.models.base import BaseModel
from app.extensions import db

class Mentor(BaseModel):
    __tablename__ = 'mentors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    about = db.Column(db.Text, nullable=True)
    photo = db.Column(db.String(255), nullable=True)

    courses = db.relationship('Course', backref='mentor', lazy=True)