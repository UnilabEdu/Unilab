from flask_restx import Resource, abort

from app.endpoints.news import news_ns, news_model
from app.models import News

@news_ns.route("/news")
class NewsApi(Resource):
    @news_ns.marshal_with(news_model)
    def get(self):
        news = News.query.all()
        return news


@news_ns.route('/news/<int:id>')
class NewsDetail(Resource):
    @news_ns.marshal_with(news_model)
    def get(self, id):
        news = News.query.get(id)
        if not news:
            abort(message="სიახლე ვერ მოიძებნა")
        return news