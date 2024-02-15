from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI", "postgresql+psycopg://user:qwerty@localhost:5432/shop")


class Config:
    TESTING = False
    SECFET_KAY = ""
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = "..."


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = "1f885984ce42bab3"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True