from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from config import config

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'admin.login'

db = SQLAlchemy()
moment = Moment()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)
    db.init_app(app)
    moment.init_app(app)

    # attach routes and custom error pages
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app