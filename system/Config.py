import os
class Config:
    SECRET_KEY = "kdshfjsdlfjldsjfldsjfljdlssjfl"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQL_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    broker_url = os.environ.get("redis_config")
    result_backend = os.environ.get("redis_config")