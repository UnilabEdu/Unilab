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


class CourseView(SecureModelView):
    create_modal = False
    edit_modal = False

    can_delete = True
    can_create = True
    can_edit = True

    column_list = ["image", "title", "description", "type", "syllabus_link", "mentor"]

    column_labels = {
        "image": "ფოტო",
        "title": "დასახელება",
        "description": "აღწერა",
        "type": "ტიპი",
        "syllabus_link": "სილაბუსი",
        "registration_link": "რეგისტრაცია",
        "mentor": "ხელმძღვანელი",
    }

    column_formatters = {
        "image": lambda v, c, m, n: Markup(
            f"<img src='/static/upload/{m.image}' width=100 "
            f"style='border-radius:6px; object-fit:cover; height:65px;'/>"
        ) if m.image else Markup("<span style='color:#aaa'>ფოტო არ არის</span>"),
        "description": lambda v, c, m, p: (
            (m.description[:80] + "…") if m.description and len(m.description) > 80 else m.description
        ),
        "syllabus_link": lambda v, c, m, p: Markup(
            f"<a href='{m.syllabus_link}' target='_blank'>გახსნა ↗</a>"
        ) if m.syllabus_link else "—",
    }

    form_columns = ["title", "description", "image", "type", "syllabus_link", "registration_link", "mentor"]

    form_overrides = {"image": ImageUploadField}
    form_args = {
        "image": {
            "label": "ფოტო",
            "base_path": Config.UPLOAD_PATH,

            "namegen": generate_filename,
            "allowed_extensions": ["jpg", "jpeg", "png", "webp", "gif"],
        }
    }

    def on_model_delete(self, model):
        flash(f'კურსი "{model}" წაიშალა.', "success")

    def after_model_change(self, form, model, is_created):
        action = "დაემატა" if is_created else "განახლდა"
        flash(f'კურსი "{model}" წარმატებით {action}.', "success")