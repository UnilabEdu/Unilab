from flask_restx import Resource, abort

from app.endpoints.statistic import statistic_ns, statistic_model
from app.models import Statistic


@statistic_ns.route("/statistic")
class StatisticApi(Resource):
    @statistic_ns.marshal_with(statistic_model)
    def get(self):
        statistic = Statistic.query.order_by(Statistic.id.desc()).first()

        if not statistic:
            abort(404, message="სტატისტიკა ვერ მოიძებნა")
        return statistic