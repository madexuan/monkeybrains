# import sqlite3
from flask_sqlalchemy import SQLAlchemy

from server import app

db = SQLAlchemy()


def connect_db(app):
    """Connects to the specific database."""
    db.app = app
    db.init_app(app)


@app.cli.command('connectdb')
def connectdb_command():
    """Connects to the database."""
    connect_db(app)
