from app.admin_views.base import SecureModelView


class FooterInfoView(SecureModelView):
    can_create = False
    can_delete = False
    can_edit = True

    column_list = ["address", "email", "facebook", "instagram", "linkedin", "youtube"]
    form_columns = ["address", "email", "facebook", "instagram", "linkedin", "youtube"]

    column_editable_list = ["address", "email", "facebook", "instagram", "linkedin", "youtube"]

    column_labels = {
        "address": "მისამართი",
        "email": "ელ. ფოსტა",
        "facebook": "Facebook",
        "instagram": "Instagram",
        "linkedin": "LinkedIn",
        "youtube": "YouTube",
    }