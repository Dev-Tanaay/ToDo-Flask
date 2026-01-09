from flask import Flask
from app.config import DevelopmentConfig
from app.routes import user,todo
from app import models
from .extensions import db,migrate

def create_app(config_class=None):
    app = Flask(__name__)
    if config_class is None:
        config_class = DevelopmentConfig
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(user,url_prefix="/api/user")
    app.register_blueprint(todo,url_prefix="/api/todo")

    return app