from flask import request
import flask_login
from sqlalchemy.orm.exc import NoResultFound
import binascii
import json
import os

from server import app
from .model import Coach
from api.database import db


@app.route('/coach')
def get_coach():
    coach_janet = Coach.query.filter(Coach.email == 'janet@example.com').one()
    return coach_janet.email


@app.route('/api/login', methods=['POST'])
def process_login():
    response = request.get_json()
    email = response.get('email')
    password = response.get('password')

    error_message = {'error': 'Email and Password combination not recognized.'}

    try:
        coach = Coach.query.filter_by(email=email).one()
        password_entered_hash = str(hash(coach.password_salt + password))
        if str(coach.password_hash) != password_entered_hash:
            return json.dumps(error_message)
        else:
            flask_login.login_user(coach)
            return json.dumps({'success': email})

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

    salt = binascii.hexlify(os.urandom(7))
    salt = salt.decode()

    error_message = {'error': 'Registration failed'}

    try:
        new_coach = Coach(
            email=email,
            name_first=name_first,
            name_last=name_last,
            password_salt=salt,
            password_hash=hash(salt + password),
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
    salt = binascii.hexlify(os.urandom(7))
    salt = salt.decode()

    error_message = {'error': 'Reset password failed'}

    try:
        coach = Coach.query.filter_by(email=email).one()
        coach.password_salt = salt
        coach.password_hash = hash(salt + password)
        db.session.commit()

        return json.dumps({'success': email})

    except NoResultFound:
        return json.dumps(error_message)


@app.route('/api/logout', methods=['POST'])
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return json.dumps({'success': 'logged out'})
