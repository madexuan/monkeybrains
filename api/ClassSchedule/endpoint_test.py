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


class ClassScheduleTestCase(unittest.TestCase, LoginTestMixin):

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

    def test_get_class_schedule(self):
        response = self.app.get('/api/class_schedule')

        # convert data from byte to string
        data = response.data.decode('utf-8')
        print(data)
        response = json.loads(data)
        assert response[0]['name'] == 'Youth Jiu Jitsu'
        assert response[0]['time'] == '05:00 PM'
        assert response[0]['day_of_week'] == 'Monday'

    def test_get_class_instance(self):
        response = self.app.get('/api/class_instance/1')

        # convert data from byte to string
        data = response.data.decode('utf-8')
        print(data)
        response = json.loads(data)
        assert response['date'] == 'Mon, 05/02/16'
        assert response['substitute_coach_id'] == None

    def test_get_class_instance_with_incorrect_id(self):
        response = self.app.get('/api/class_instance/10')

        # convert data from byte to string
        data = response.data.decode('utf-8')
        print(data)
        response = json.loads(data)
        assert response == {}


if __name__ == '__main__':
    unittest.main()
