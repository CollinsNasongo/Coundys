from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Import models so SQLAlchemy sees them
    from . import models

    # Register routes
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
