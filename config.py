import os 
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "50m3h@rd2gu355t3xt"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///" + os.path.join(base_dir, "data-dev.sqlite")

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite://"

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")

config = {
    "development" : DevelopmentConfig,
    "testing" : TestConfig,
    "production" : ProductionConfig,

    "default" : DevelopmentConfig
} 
