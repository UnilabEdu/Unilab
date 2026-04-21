from flask_restx import fields
from app.extensions import api

faq_ns = api.namespace("FAQ", path='/api')

faq_model = faq_ns.model("FAQ", {
    "id": fields.Integer,
    "order_num": fields.Integer,
    "question": fields.String,
    "answer": fields.String,
})

