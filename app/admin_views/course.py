from app.admin_views.base import SecureModelView
from wtforms_sqlalchemy.fields import QuerySelectField
from app.extensions import db

class CourseView(SecureModelView):
    create_modal = True

    column_formatters = {
        'description': lambda v, c, m, p: (m.description[:80] + '...') if m.description and len(m.description) > 80 else m.description
    }

    form_columns = ["title", "description", "syllabus_link", "type", "registration_link", "mentor"]

    form_extra_fields = {
        "mentor": QuerySelectField(
            "Mentor",
            query_factory=lambda: db.session.query(__import__("app.models.mentor").models.mentor.Mentor).all(),
            allow_blank=True,
            get_label="name"
        )
    }