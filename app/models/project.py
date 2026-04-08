from app.models.base import BaseModel
from app.extensions import db

class Project(BaseModel):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=True)
    link = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), nullable=False)

    course = db.relationship("Course", backref="projects")
    users = db.relationship("ProjectUser", back_populates="project", cascade="all, delete-orphan")

    def __str__(self):
        return self.name


class ProjectUser(BaseModel):
    __tablename__ = 'project_users'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    project = db.relationship("Project", back_populates="users")
    user = db.relationship("User", backref="project_users")

    def __str__(self):
        return f"ProjectUser(project={self.project_id}, user={self.user_id})"