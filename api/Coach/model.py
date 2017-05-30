from flask_login import UserMixin

from api import login_manager
from api.database import db


class Coach(UserMixin, db.Model):
    """TODO"""

    __tablename__ = "coach"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(124), nullable=False, unique=True)
    name_first = db.Column(db.String(64), nullable=True, unique=True)
    name_last = db.Column(db.String(64), nullable=True, unique=True)
    password_salt = db.Column(db.String(20), nullable=True)
    password_hash = db.Column(db.String(64), nullable=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    # override UserMixin get_id method
    def get_id(self):
        return self.email

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<Coach id={} email={}>".format(self.id, self.email)


@login_manager.user_loader
def load_user(email):
    # use .first() to return None if no match
    # as per Flask-Login requirements
    return Coach.query.filter_by(email=email).first()
