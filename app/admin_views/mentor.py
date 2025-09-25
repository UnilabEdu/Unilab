from os import path
from uuid import uuid4

from markupsafe import Markup

from app import Config
from app.admin_views.base import SecureModelView
from flask_admin.form import ImageUploadField

def generate_filename(obj, file):
    name, extension = path.splitext(file.filename)
    return f"{uuid4()}{extension}"

class MentorView(SecureModelView):
    create_modal = True

    column_formatters = {
        "about": lambda v, c, m, p: (m.about[:80] + '...') if m.about and len(m.about) > 80 else m.about,
        "image": lambda  v, c, m, n: Markup(f"<img src='/static/upload/{m.image}' width=70/>")
    }
    form_overrides = {"image": ImageUploadField}
    form_args = {
        "image": {
            "base_path": Config.UPLOAD_PATH,
            "namegen": generate_filename
        }
    }