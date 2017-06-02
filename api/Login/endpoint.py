from flask import request
import flask_login
from sqlalchemy.orm.exc import NoResultFound
import json

from server import app
from api.database import db
from api.Coach.model import Coach


@app.route('/api/login', methods=['POST'])
def process_login():
    response = request.get_json()
    email = response.get('email')
    password = response.get('password')

    error_message = {'error': 'Email and Password not recognized.'}

    try:
        coach = Coach.query.filter_by(email=email).one()
        if coach.is_correct_password(password):
            flask_login.login_user(coach)
            return json.dumps({'success': email})
        else:
            return json.dumps(error_message)

    except NoResultFound:
        return json.dumps(error_message)


@app.route('/api/register', methods=['POST'])
def register():
    response = request.get_json()
    email = response.get('email')
    password = response.get('password')
    name_first = response.get('name_first')
    name_last = response.get('name_last')
    is_admin = response.get('is_admin')

    error_message = {'error': 'Registration failed'}

    try:
        new_coach = Coach(
            email=email,
            name_first=name_first,
            name_last=name_last,
            password=password,
            is_admin=is_admin)
        db.session.add(new_coach)
        db.session.commit()

        return json.dumps({'success': email})
    except:
        return json.dumps(error_message)


@app.route('/api/reset_password', methods=['POST'])
def reset_password():
    response = request.get_json()
    email = response.get('email')
    password = response.get('password')

    error_message = {'error': 'Reset password failed'}

    try:
        coach = Coach.query.filter_by(email=email).one()
        coach.password = password
        db.session.add(coach)
        db.session.commit()

        return json.dumps({'success': email})

    except NoResultFound:
        return json.dumps(error_message)


@app.route('/api/logout', methods=['POST'])
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return json.dumps({'success': 'logged out'})
