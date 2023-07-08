import os
import secrets

from pydantic import BaseSettings
from datetime import date


class Settings(BaseSettings):
    ENV = os.getenv("ENV", "dev")
    SECRET_KEY = "SuP3R_S3cReT_R0ck3T" if ENV == "dev" else secrets.token_urlsafe(32)
    SESSION_SECRET_KEY = "SuP3R_S3cReT_R0ck3T" if ENV == "dev" else secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    MONGO_CONNECTION_STRING: str = os.getenv("MONGO_CONNECTION_STRING", "mongodb://localhost:27017")
    MONGO_DATABASE_NAME: str = os.getenv("MONGO_DATABASE_NAME2", "brainbrew")
    SMTP_SENDER = "hello@brainbrew.io"
    SMTP_PASSWORD = "wfpxqzitpyltcukk"
    if os.path.exists("../build_date"):
        try:
            with open("../build_date", "r") as f:
                BUILD_DATE = f.read()
        except:
            BUILD_DATE = str(date.today().strftime("%Y-%m-%d"))
    else:
        BUILD_DATE = str(date.today().strftime("%Y-%m-%d"))
    GOOGLE_CLIENT_ID = os.getenv(
        "GOOGLE_CLIENT_ID", "581069090899-crl084g2unm4qiqi55vmh3sa879evaoo.apps.googleusercontent.com")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "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")
    FRONTEND_URL = os.environ.get('FRONTEND_URL') or 'http://localhost:8000/api/v1/auth/token'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
    UNAUTH_MIN_LENGTH = 10
    UNAUTH_MAX_LENGTH = 5000
    AUTH_MIN_LENGTH = 10
    AUTH_MAX_LENGTH = 5000

    class Config:
        case_sensitive = True


settings = Settings()
