from datetime import datetime

from api.Base.helper import to_json
from server import app

from .model import ClassSchedule
from .model import ClassInstance


@app.route('/class_schedule')
def get_class_schedule():
    class_schedule = ClassSchedule.query.all()
    result = to_json(class_schedule)
    return result


@app.route('/class_instance')
def get_class_instance():
    class_instance = ClassInstance.query.filter(ClassInstance.date == '05/07/2016').one()
    class_instance_formatted = datetime.strftime(class_instance.date, '%a, %m/%d/%y')
    return class_instance_formatted
