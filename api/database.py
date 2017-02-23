from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connects to the specific database."""
    db.app = app
    db.init_app(app)
