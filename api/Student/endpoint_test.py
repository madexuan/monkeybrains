import unittest
import json

from api.Base.endpoint_test import BaseTestCase


class ApiTestCase(BaseTestCase):

    logged_in = True

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
