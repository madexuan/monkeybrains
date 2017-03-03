from sqlalchemy.orm.exc import NoResultFound

from api.Base.helper import to_json
from server import app

from .model import ClassSchedule
from .model import ClassInstance


@app.route('/api/class_schedule')
def get_class_schedule():
    class_schedule = ClassSchedule.query.all()
    result = to_json(class_schedule)
    return result


@app.route('/api/class_instance/<int:id>')
def get_class_instance(id):
    try:
        class_instance = ClassInstance.query.filter(ClassInstance.id == id).one()
    except NoResultFound:
        class_instance = {}

    class_instance = to_json(class_instance)

    return class_instance
