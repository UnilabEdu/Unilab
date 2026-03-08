from app.admin_views.base import SecureModelView

class CourseView(SecureModelView):
    create_modal = True

    column_formatters = {
        'description': lambda v, c, m, p: (m.description[:80] + '...') if m.description and len(m.description) > 80 else m.description
    }

    form_columns = ["title", "description", "syllabus_link", "type", "registration_link", "mentor"]