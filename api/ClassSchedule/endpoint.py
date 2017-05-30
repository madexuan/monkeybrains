from sqlalchemy.orm.exc import NoResultFound
import flask_login

from api.Base.helper import to_json
from server import app

from .model import ClassSchedule
from .model import ClassInstance


@app.route('/api/class_schedule')
@flask_login.login_required
def get_class_schedule():
    class_schedule = ClassSchedule.query.all()
    result = to_json(class_schedule)
    return result


@app.route('/api/class_instance/<int:id>')
@flask_login.login_required
def get_class_instance(id):
    try:
        class_instance = ClassInstance.query.filter(ClassInstance.id == id).one()
    except NoResultFound:
        class_instance = {}

    class_instance = to_json(class_instance)

    return class_instance
