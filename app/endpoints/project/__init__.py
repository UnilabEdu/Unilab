from flask_restx import fields
from app.extensions import api

project_ns = api.namespace("Project", path='/api')

project_model = project_ns.model("Project", {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
    "image": fields.String,
    "link": fields.String,
    "course_id": fields.Integer,
})