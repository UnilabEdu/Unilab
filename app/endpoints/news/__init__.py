from flask_restx import fields

from app.extensions import api

news_ns = api.namespace("News", path='/api')

news_model = news_ns.model("News", {
    "id": fields.Integer,
    "title": fields.String,
    "description": fields.String,
    "image": fields.String,
    "date_created": fields.DateTime
})