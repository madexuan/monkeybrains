import unittest
import json

from api.Base.endpoint_test import BaseTestCase


class ClassScheduleTestCase(BaseTestCase):

    logged_in = True

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
