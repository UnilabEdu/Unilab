from os import path
from uuid import uuid4

from markupsafe import Markup
from flask import flash

from app import Config
from app.admin_views.base import SecureModelView
from flask_admin.form import ImageUploadField


def generate_filename(obj, file):
    name, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"

class MentorView(SecureModelView):
    create_modal = False
    edit_modal = False

    can_delete = True
    can_create = True
    can_edit = True

    column_list = ["image", "name", "about"]

    column_labels = {
        "image": "ფოტო",
        "name": "სახელი და გვარი",
        "about": "მცირე აღწერა",
    }

    column_formatters = {
        "image": lambda v, c, m, n: Markup(
            f"<img src='/static/upload/{m.image}' width=70 "
            f"style='border-radius:50%; object-fit:cover; height:70px;'/>"
        ) if m.image else Markup("<span style='color:#aaa'>ფოტო არ არის</span>"),
        "about": lambda v, c, m, p: (
            (m.about[:80] + "…") if m.about and len(m.about) > 80 else m.about
        ),
    }

    form_columns = ["name", "about", "image"]

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
        flash(f'ხელმძღვანელი "{model}" წაიშალა.', "success")

    def after_model_change(self, form, model, is_created):
        action = "დაემატა" if is_created else "განახლდა"
        flash(f'ხელმძღვანელი "{model}" წარმატებით {action}.', "success")


