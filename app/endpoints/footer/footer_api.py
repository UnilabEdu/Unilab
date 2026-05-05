from flask_restx import Resource, abort

from app.endpoints.footer import footer_ns, footer_model
from app.models import FooterInfo


@footer_ns.route("/footer")
class FooterApi(Resource):
    @footer_ns.marshal_with(footer_model)
    def get(self):
        footer = FooterInfo.query.first()

        if not footer:
            abort(404, message="ფუტერის ინფო ვერ მოიძებნა")
        return footer