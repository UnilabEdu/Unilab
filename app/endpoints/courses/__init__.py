from flask_restx import fields

from app.extensions import api

course_ns = api.namespace("Courses", description="Course endpoints", path='/api')

mentor_model = course_ns.model("Mentor", {
    "id": fields.Integer,
    "name": fields.String,
    "about": fields.String,
    "photo": fields.String
})

courses_model = course_ns.model("Course", {
    "id": fields.Integer,
    "title": fields.String,
    "description": fields.String,
    "syllabus_link": fields.String,
    "type": fields.String,
    "registration_link": fields.String,
    "mentor": fields.Nested(mentor_model)
})