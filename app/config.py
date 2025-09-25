import os
from os import path
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))

    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret")
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.example.com")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")

    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static", "upload")