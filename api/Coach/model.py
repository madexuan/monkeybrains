from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from api import login_manager, bcrypt
from api.database import db


class Coach(UserMixin, db.Model):
    """TODO"""

    __tablename__ = "coach"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(124), nullable=False, unique=True)
    email_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    name_first = db.Column(db.String(64), nullable=False)
    name_last = db.Column(db.String(64), nullable=False)
    _password = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext).decode('utf-8')

    # override UserMixin get_id method
    def get_id(self):
        return self.email

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<Coach id={} email={}>".format(self.id, self.email)


@login_manager.user_loader
def load_user(email):
    # use .first() to return None if no match
    # as per Flask-Login requirements
    return Coach.query.filter_by(email=email).first()
