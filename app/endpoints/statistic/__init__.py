from flask_restx import fields
from app.extensions import api


statistic_ns = api.namespace("Statistic", path='/api')

statistic_model = statistic_ns.model("Statistic", {
    "id": fields.Integer,
    "course_count": fields.Integer,
    "student_count": fields.Integer,
    "intern_count": fields.Integer,
    "certificate_count": fields.Integer,
})