from flask_restx import fields
from app.extensions import api

footer_ns = api.namespace("Footer", path='/api')


footer_model = footer_ns.model("Footer", {
    "id": fields.Integer,
    "address": fields.String,
    "email": fields.String,
    "facebook": fields.String,
    "instagram": fields.String,
    "linkedin": fields.String,
    "youtube": fields.String,
})