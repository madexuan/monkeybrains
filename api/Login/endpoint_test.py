import unittest

from api.Base.endpoint_test import BaseTestCase


class LoginTestCase(BaseTestCase):

    def test_login_flow(self):
        # REGISTER
        # succeeds with new email and password combo
        register_success = self.register('janet1@example.com',
                                         'default',
                                         'janet',
                                         'last_name',
                                         True)
        assert b'janet1@example.com' in register_success.data

        # fails if email already registered
        register_fail = self.register('janet@example.com',
                                      'default',
                                      'janet',
                                      'last_name',
                                      True)
        assert b'Registration failed' in register_fail.data

        # RESET PASSWORD
        reset_password_success = self.reset_password('janet@example.com', 'newpassword')
        assert b'janet@example.com' in reset_password_success.data
        reset_password_fail = self.reset_password('janet2@example.com', 'default')
        assert b'Reset password failed' in reset_password_fail.data

        # LOGIN
        login_success = self.login('janet@example.com', 'newpassword')
        assert b'janet@example.com' in login_success.data
        login_fail = self.login('idontexist@example.com', 'hacker')
        assert b'Email and Password not recognized' in login_fail.data

        # LOGOUT
        logout = self.logout()
        assert b'logged out' in logout.data


if __name__ == '__main__':
    unittest.main()
