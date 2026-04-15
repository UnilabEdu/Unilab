from app.models.base import BaseModel
from app.extensions import db

class Statistic(BaseModel):
    __tablename__ = 'statistics'

    id = db.column(db.Integer, primary_key = True)
    course_count = db.Column(db.Integer, default = 0 , nullable = False)
    student_count = db.Column(db.Integer, default = 0, nullable = False)
    intern_count = db.Column(db.Integer, default = 0, nullable = False)
    certificate_count = db.Column(db.Integer, default = 0, nullable = False)


    def __str__(self):
        return "სტატისტიკა"

    
