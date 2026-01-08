from flask import Flask
from app.config import DevelopmentConfig
from app.routes import user

def create_app(config_class=None):
    app = Flask(__name__)
    if config_class is None:
        config_class = DevelopmentConfig
    app.config.from_object(config_class)

    app.register_blueprint(user,url_prefix="/api")
    return app