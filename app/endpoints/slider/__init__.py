from flask_restx import fields
from app.extensions import api

slider_ns = api.namespace("slider", path='/api')


slider_model = slider_ns.model("slider", {
    "id": fields.Integer,
    "image": fields.String,
    "title": fields.String,
    "subtitle": fields.String,
    "order": fields.Integer,
})

