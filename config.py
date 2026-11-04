import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "defect-predictor-secret-key-2026")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-super-secret-key-defect-ai")
    DATABASE_PATH = os.getenv("DATABASE_PATH", "database/defect_prediction.db")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
    REPORT_FOLDER = os.getenv("REPORT_FOLDER", "reports")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USER = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", "noreply@defect-predictor.org")
