import os
import unittest
import tempfile
import json

from server import app
from api.database import db, connect_db
from seed_database import (load_student, load_coach, load_class_schedule,
                           load_class_instance, load_student_class_instance,
                           load_student_class_schedule)


class ApiTestCase(unittest.TestCase):

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

    def test_get_student_class_schedule(self):
        response = self.app.get('/student_class_schedule')

        # convert data from byte to string
        data = response.data.decode('utf-8')
        response = json.loads(data)
        assert response[0]['student_id'] == 1
        assert response[0]['class_schedule_id'] == 3


if __name__ == '__main__':
    unittest.main()
