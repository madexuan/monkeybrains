import unittest
from unittest.mock import patch

from api.Base.endpoint_test import BaseTestCase
from api.Coach.model import Coach
from .utils import ts


class LoginTestCase(BaseTestCase):

    # don't actually send the email when registering
    @patch('api.Login.endpoint.send_email', return_value=None)
    def test_login_flow(self, mock_send_email):
        janet = 'janet@example.com'
        janet1 = 'janet1@example.com'
        janet2 = 'janet2@example.com'
        janetb = janet.encode('utf-8')
        janet1b = janet1.encode('utf-8')

        # REGISTER
        # succeeds with new email and password combo
        register_success = self.register(janet1,
                                         'default',
                                         'janet',
                                         'last_name',
                                         True)
        assert janet1b in register_success.data
        assert mock_send_email.called

        # fails if email already registered
        register_fail = self.register(janet,
                                      'default',
                                      'janet',
                                      'last_name',
                                      True)
        assert b'Registration failed' in register_fail.data

        # CONFRIM EMAIL
        token = ts.dumps(janet1, salt='email-confirm-key')

        confirm_email_success = self.confirm(token)
        assert b'janet1@example.com' in confirm_email_success.data
        confirmed_coach = Coach.query.filter_by(email=janet1).one()
        assert confirmed_coach.email_confirmed == True

        # RESET PASSWORD
        reset_password_success = self.reset_password(janet, 'newpassword')
        assert janetb in reset_password_success.data
        reset_password_fail = self.reset_password(janet2, 'default')
        assert b'Reset password failed' in reset_password_fail.data

        # LOGIN
        login_success = self.login(janet, 'newpassword')
        assert janetb in login_success.data
        login_fail = self.login('idontexist@example.com', 'hacker')
        assert b'Email and Password not recognized' in login_fail.data

        # LOGOUT
        logout = self.logout()
        assert b'logged out' in logout.data


if __name__ == '__main__':
    unittest.main()
