from app.models.base import BaseModel
from app.extensions import db


class FrequentlyAskedQuestion(BaseModel):
    __tablename__ = 'faqs'

    id = db.Column(db.Integer, primary_key=True)
    order_num = db.Column(db.Integer, default=0, nullable=False)
    question = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.Text, nullable=False)

    def __str__(self):
        return self.question