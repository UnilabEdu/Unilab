from flask_restx import Resource

from app.endpoints.slider import slider_ns, slider_model
from app.models import Slider


@slider_ns.route("/sliders")
class SliderApi(Resource):
    @slider_ns.marshal_with(slider_model)
    def get(self):
        return Slider.query.filter_by(is_active=True).order_by(Slider.order).all()