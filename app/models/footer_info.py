from app.models.base import BaseModel
from app.extensions import db

class FooterInfo(BaseModel):

    __tablename__ = "footer_info"

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    facebook = db.Column(db.String(255), nullable=True)
    instagram = db.Column(db.String(255), nullable=True)
    linkedin = db.Column(db.String(255), nullable=True)
    youtube = db.Column(db.String(255), nullable=True)

    def __str__(self):
        return "ფუტერის ინფო"


