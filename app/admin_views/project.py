from os import path
from uuid import uuid4

from markupsafe import Markup
from flask import flash

from app import Config
from app.admin_views.base import SecureModelView
from flask_admin.form import ImageUploadField


def generate_filename(obj, file):
    _, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"


class ProjectView(SecureModelView):
    create_modal = False
    edit_modal = False

    can_delete = True
    can_create = True
    can_edit = True

    column_list = ["image", "name", "course", "link", "description"]

    column_labels = {
        "image": "ფოტო",
        "name": "სახელი",
        "course": "კურსი",
        "link": "ლინკი",
        "description": "აღწერა",
    }

    column_formatters = {
        "image": lambda v, c, m, n: Markup(
            f"<img src='/static/upload/{m.image}' width=100 "
            f"style='border-radius:6px; object-fit:cover; height:65px;'/>"
        ) if m.image else Markup("<span style='color:#aaa'>ფოტო არ არის</span>"),
        "description": lambda v, c, m, p: (
            (m.description[:80] + "…") if m.description and len(m.description) > 80 else m.description
        ),
    }

    form_columns = ["name", "course", "link", "description", "image"]

    form_overrides = {"image": ImageUploadField}
    form_args = {
        "image": {
            "label": "ფოტო",
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename,
            "allowed_extensions": ["jpg", "jpeg", "png", "webp", "gif"],
        }
    }

    # Confirmation message on delete
    delete_template = "admin/delete_confirmation.html"

    def on_model_delete(self, model):
        flash(f'პროექტი "{model}" წაიშალა.', "success")

    def after_model_change(self, form, model, is_created):
        action = "დაემატა" if is_created else "განახლდა"
        flash(f'პროექტი "{model}" წარმატებით {action}.', "success")