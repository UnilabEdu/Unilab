from app.admin_views.base import SecureModelView


class StatisticView(SecureModelView):
    can_create = False
    can_delete = False
    can_edit = True

    column_editable_list = ["course_count", "student_count", "intern_count", "certificate_count"]

    column_labels = {
        "course_count": "კურსების რაოდენობა",
        "student_count": "სტუდენტების რაოდენობა",
        "intern_count": "აქსელერაციის მონაწილეთა რაოდენობა",
        "certificate_count": "გაცემული სერტიფიკატების რაოდენობა",
    }

    column_list = ["course_count", "student_count", "intern_count", "certificate_count"]
    form_columns = ["course_count", "student_count", "intern_count", "certificate_count"]