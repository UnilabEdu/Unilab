from app.models.base import BaseModel
from app.extensions import db

class Slider(BaseModel):
    __tablename__ = "slider"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(200), nullable=True)
    subtitle = db.Column(db.String(400), nullable=True)
    order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)

    def __str__(self):
        return self.title or f"Slide #{self.id}"
