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


class ApiTestCase(unittest.TestCase, LoginTestMixin):

    def setUp(self):
        self.db_fd, self.db_filename = tempfile.mkstemp()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/monkeystest'
        app.config['TESTING'] = True
        app.testing = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        connect_db(app)
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
        self.logout()

    def test_get_student_class_schedule(self):
        response = self.app.get('/api/student_class_schedule')

        # convert data from byte to string
        data = response.data.decode('utf-8')
        response = json.loads(data)
        assert response[0]['student_id'] == 1
        assert response[0]['class_schedule_id'] == 3

    def test_get_students(self):
        response = self.app.get('/api/students')

        # convert data from byte to string
        data = response.data.decode('utf-8')
        response = json.loads(data)
        assert response[0]['id'] == 1
        assert response[0]['name_first'] == 'Paul'
        assert response[-1]['name_first'] == 'George'
        assert response[-1]['rank_type'] == 'white'

    def test_get_student_class_instance(self):
        response = self.app.get('/api/student_class_instance/1')

        # convert data from byte to string
        data = response.data.decode('utf-8')
        response = json.loads(data)
        assert response[0]['id'] == 1
        assert response[0]['attendance'] == 'P'
        assert response[0]['student_id'] == 1

    def test_get_student_class_instance_incorrect_id(self):
        response = self.app.get('/api/student_class_instance/100')

        # convert data from byte to string
        data = response.data.decode('utf-8')
        response = json.loads(data)
        assert response == []

    def test_update_student_class_instance_attendance(self):
        response = self.app.get('/api/student_class_instance/1/T')

        # convert data from byte to string
        data = response.data.decode('utf-8')
        response = json.loads(data)
        assert response == {'student_id': 1, 'id': 1, 'class_instance_id': 1, 'attendance': 'T', 'notes': None}


if __name__ == '__main__':
    unittest.main()
