from os import path
from uuid import uuid4

from markupsafe import Markup

from app import Config
from app.admin_views.base import SecureModelView
from flask_admin.form import ImageUploadField


def generate_filename(obj, file):
    name, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"


class SliderView(SecureModelView):
    create_modal = True
    edit_modal = True

    column_list = ["image", "title", "subtitle", "order", "is_active"]

    column_labels = {
        "image": "ფოტო",
        "title": "სათაური",
        "subtitle": "ქვესათაური",
        "order": "თანმიმდევრობა",
        "is_active": "აქტიური"
    }

    column_formatters = {
        "image": lambda v, c, m, n: Markup(f"<img src='/static/upload/{m.image}' width=120 style='border-radius:4px'/>"),
        "subtitle": lambda v, c, m, p: (m.subtitle[:80] + '...') if m.subtitle and len(m.subtitle) > 80 else m.subtitle
    }

    form_columns = ["image", "title", "subtitle", "order", "is_active"]

    form_overrides = {"image": ImageUploadField}
    form_args = {
        "image": {
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename
        }
    }