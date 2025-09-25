from flask_restx import Resource

from app.endpoints.courses import course_ns, courses_model
from app.models import Course

@course_ns.route("/courses")
class CourseApi(Resource):
    @course_ns.marshal_with(courses_model)
    def get(self):
        courses = Course.query.all()
        return courses


@course_ns.route('/course/<int:id>')
class CourseDetail(Resource):
    def get(self, id):
        course = Course.query.get(id)
        if not course:
            return {"message": "კურსი ვერ მოიძებნა"}, 404

        return {
            "id": course.id,
            "title": course.title,
            "description": course.description,
            "mentor_name": course.mentor.name if course.mentor else None,
            "type": course.type,
            "syllabus_link": course.syllabus_link,
            "registration_link": course.registration_link
        }, 200