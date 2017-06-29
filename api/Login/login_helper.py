import json


class LoginTestMixin:
    def reset_password(self, email, password):
        return self.app.post('/api/reset_password',
                             data=json.dumps(dict(
                                email=email,
                                password=password
                             )),
                             content_type='application/json')

    def login(self, email, password):
        return self.app.post('/api/login',
                             data=json.dumps(dict(
                                 email=email,
                                 password=password
                             )),
                             content_type='application/json')

    def register(self, email, password, name_first, name_last, is_admin):
        return self.app.post('/api/register',
                             data=json.dumps(dict(
                                email=email,
                                password=password,
                                nameFirst=name_first,
                                nameLast=name_last,
                                is_admin=is_admin,
                             )),
                             content_type='application/json')

    def confirm(self, token):
        return self.app.get('/api/confirm/' + token)

    def logout(self):
        return self.app.post('/api/logout')

    def fake_login(self):
        email = 'janet@example.com'
        password = 'newpassword'
        self.reset_password(email, password)
        self.login(email, password)
