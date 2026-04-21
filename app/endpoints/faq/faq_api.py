from flask_restx import Resource, abort

from app.endpoints.faq import faq_ns, faq_model
from app.models import FrequentlyAskedQuestion


@faq_ns.route("/faqs")
class FAQApi(Resource):
    @faq_ns.marshal_with(faq_model)
    def get(self):
        return FrequentlyAskedQuestion.query.order_by(FrequentlyAskedQuestion.order_num).all()


@faq_ns.route("/faq/<int:id>")
class FAQDetail(Resource):
    @faq_ns.marshal_with(faq_model)
    def get(self, id):
        faq = FrequentlyAskedQuestion.query.get(id)
        if not faq:
            abort(404, message="FAQ ვერ მოიძებნა")
        return faq