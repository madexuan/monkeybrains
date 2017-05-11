import os
import unittest
import tempfile

from server import app
from api.database import db, connect_db
from seed_database import (load_student, load_coach, load_class_schedule,
                           load_class_instance, load_student_class_instance,
                           load_student_class_schedule)


class CoachTestCase(unittest.TestCase):

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

    def login(self, email, password):
        return self.app.post('/api/process_login', data=dict(
            email=email,
            password=password
        ))

    def test_login(self):
        login_success = self.login('janet@example.com', 'default')
        assert b'janet@example.com' in login_success.data
        login_fail = self.login('idontexist@example.com', 'hacker')
        assert b'Email and Password not recognized. Please re-enter' in login_fail.data


if __name__ == '__main__':
    unittest.main()
