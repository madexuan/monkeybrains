from itsdangerous import URLSafeTimedSerializer
from sendgrid.helpers.mail import Mail, Email, Content

from api import sg
from server import app

ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])


def send_email(email, subject, html):
    msg = create_email(email, subject, html)
    request_body = msg.get()
    response = _send_email(request_body)
    print(response.status_code)
    print(response.body)
    print(response.headers)


def _send_email(request_body):
    """Wrapping the SendGrid mail sending method in order to patch it
    while testing. https://github.com/sendgrid/sendgrid-python/issues/293"""
    response = sg.client.mail.send.post(request_body=request_body)
    return response


def create_email(email, subject, html):
    from_email = Email("jskenmotsu@gmail.com")
    to_email = Email(email)
    content = Content("text/html", html)
    msg = Mail(from_email, subject, to_email, content)
    return msg
