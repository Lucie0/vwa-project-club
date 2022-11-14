import os


class BaseConfig(object):
    pass


class DevelopmentConfig(BaseConfig):
    ENV = "development"
    DEBUG = True
    SECRET_KEY = "Sveřepí šakali zavile vyli na bílý měsíc"


class ProductionConfig(BaseConfig):
    ENV = "production"
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
