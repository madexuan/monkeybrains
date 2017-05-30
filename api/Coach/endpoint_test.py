import os
import unittest
import tempfile
import json

from server import app
from api.database import db, connect_db
from api.Base.login_helper import LoginTestMixin
from seed_database import (load_student, load_coach, load_class_schedule,
                           load_class_instance, load_student_class_instance,
                           load_student_class_schedule)


class CoachTestCase(unittest.TestCase, LoginTestMixin):

    def setUp(self):
        self.db_fd, self.db_filename = tempfile.mkstemp()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/monkeystest'
        app.config['TESTING'] = True
        app.testing = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        connect_db(app)

        with app.app_context():
            db.drop_all()
            db.create_all()
            load_student()
            load_coach()
            load_class_schedule()
            load_class_instance()
            load_student_class_instance()
            load_student_class_schedule()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_filename)

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
        assert b'Email and Password combination not recognized' in login_fail.data

        # LOGOUT
        logout = self.logout()
        assert b'logged out' in logout.data

if __name__ == '__main__':
    unittest.main()
