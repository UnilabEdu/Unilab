from flask import flash
from app.admin_views.base import SecureModelView


class FAQView(SecureModelView):
    can_create = True
    can_edit = True
    can_delete = True

    column_default_sort = ('order_num', False)

    column_list = ["order_num", "question", "answer"]
    form_columns = ["order_num", "question", "answer"]

    column_editable_list = ["order_num", "question"]

    column_labels = {
        "order_num": "თანმიმდევრობა",
        "question": "შეკითხვა",
        "answer": "პასუხი",
    }

    column_formatters = {
        "answer": lambda v, c, m, p: (m.answer[:80] + "…") if m.answer and len(m.answer) > 80 else m.answer,
    }

    def on_model_delete(self, model):
        flash(f'FAQ "{model}" წაიშალა.', "success")

    def after_model_change(self, form, model, is_created):
        action = "დაემატა" if is_created else "განახლდა"
        flash(f'FAQ "{model}" წარმატებით {action}.', "success")
