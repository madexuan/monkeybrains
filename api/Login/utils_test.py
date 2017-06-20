from .utils import send_email, create_email
from api.Base.fixtures import email, subject, html
from flask_mail import Message

from unittest.mock import patch


@patch('api.Login.utils.mail.send')
def test_send_email(mock_mail_send):
    send_email(email, subject, html)
    assert mock_mail_send.called


def test_create_email():
    test_email = create_email(email, subject, html)
    expected = Message(
        subject=subject,
        html=html,
        sender='jskenmotsu@gmail.com',
        recipients=[email])

    assert test_email.html == expected.html
    assert test_email.subject == expected.subject
    assert test_email.sender == expected.sender
    assert test_email.recipients == expected.recipients
