from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message

from api import mail
from server import app


ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])


def send_email(email, subject, html):
    msg = create_email(email, subject, html)
    mail.send(msg)


def create_email(email, subject, html):
    msg = Message(
        subject=subject,
        html=html,
        sender='jskenmotsu@gmail.com',
        recipients=[email])
    return msg
