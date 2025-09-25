from os import path
from uuid import uuid4

from markupsafe import Markup

from app import Config
from app.admin_views.base import SecureModelView
from flask_admin.form import ImageUploadField

def generate_filename(obj, file):
    name, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"

class NewsView(SecureModelView):
    create_modal = True

    column_formatters = {
        'description': lambda v, c, m, p: (m.description[:80] + '...') if m.description and len(m.description) > 80 else m.description,
        "image": lambda v, c, m, n: Markup(f"<img src='/static/upload/{m.image}' width=70/>")
    }
    form_overrides = {"image": ImageUploadField}
    form_args = {
        "image": {
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename
        }
    }