from flask import request
from sqlalchemy.orm.exc import NoResultFound

import json
from server import app
from .model import Coach


@app.route('/coach')
def get_coach():
    coach_janet = Coach.query.filter(Coach.email == 'janet@example.com').one()
    return coach_janet.email


@app.route('/api/process_login', methods=['POST'])
def process_login():
    email = request.form.get("email")
    # password = request.form.get("password")

    error_message = {'error': 'Email and Password not recognized. Please re-enter.'}

    try:
        coach = Coach.query.filter_by(email=email).one()
        return json.dumps({'success': email})
        # password_entered_hash = str(hash(coach.password_salt + password))
        # if str(coach.password_hash) != password_entered_hash:
        #     return json.dumps(error_message)
        # else:
        #     return json.dumps({'success': 'yay'})

    except NoResultFound:
        return json.dumps(error_message)
