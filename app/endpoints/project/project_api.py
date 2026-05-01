from flask_restx import Resource, abort

from app.endpoints.project import project_ns, project_model
from app.models import Project


@project_ns.route("/projects")
class ProjectApi(Resource):
    @project_ns.marshal_with(project_model)
    def get(self):
        return Project.query.all()


@project_ns.route("/projects/<int:id>")
class ProjectDetail(Resource):
    @project_ns.marshal_with(project_model)
    def get(self, id):
        project = Project.query.get(id)
        if not project:
            abort(404, message="პროექტი ვერ მოიძებნა")
        return project