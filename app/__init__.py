from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config

from app import db


def create_app():
    """Creamos la aplicación basada en flask
    
    También se inicia la base de datos configurada en
    app/db.py y se inicia la conexión con Bootstrap

    Returns:
        app: aplicación flask
    """
    db.Base.metadata.create_all(db.engine)
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    return app