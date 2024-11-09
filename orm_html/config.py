
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "1234"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        'postgresql://{user}:{password}@{host}:5432/{dbname}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
