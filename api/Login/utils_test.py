from .utils import send_email, create_email
from api.Base.fixtures import email, subject, html
from sendgrid.helpers.mail import Mail, Email, Content

from unittest.mock import patch


@patch('api.Login.utils._send_email')
def test_send_email(mock_mail_send):
    send_email(email, subject, html)
    assert mock_mail_send.called


def test_create_email():
    test_email = create_email(email, subject, html)
    from_email = Email("jskenmotsu@gmail.com")
    to_email = Email(email)
    content = Content("text/html", html)
    expected = Mail(from_email, subject, to_email, content)

    assert test_email.from_email.email == expected.from_email.email
    assert test_email.personalizations[0].tos[0]['email'] == expected.personalizations[0].tos[0]['email']
    assert test_email.contents[0].value == expected.contents[0].value
    assert test_email.subject == expected.subject
