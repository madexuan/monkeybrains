import os
import unittest
import tempfile

from server import app
from api.database import db, connect_db
from api.Login.login_helper import LoginTestMixin
from seed_database import (load_student, load_coach, load_class_schedule,
                           load_class_instance, load_student_class_instance,
                           load_student_class_schedule)


class BaseTestCase(unittest.TestCase, LoginTestMixin):

    logged_in = False

    def setUp(self):
        self.db_fd, self.db_filename = tempfile.mkstemp()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/monkeystest'
        app.config['TESTING'] = True
        app.testing = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        connect_db(app)

        if self.logged_in:
            self.fake_login()

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
        if self.logged_in:
            self.logout()


if __name__ == '__main__':
    unittest.main()
