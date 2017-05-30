from server import app
from .model import Coach


@app.route('/coach')
def get_coach():
    coach_janet = Coach.query.filter(Coach.email == 'janet@example.com').one()
    return coach_janet.email
