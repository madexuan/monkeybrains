from sqlalchemy.orm.exc import NoResultFound
import flask_login

from server import app
from api.Base.helper import to_json
from api.database import db

from .model import Student, StudentClassInstance, StudentClassSchedule


@app.route('/api/students')
@flask_login.login_required
def get_students():
    students = Student.query.all()
    students = to_json(students)
    return students


@app.route('/api/student_class_instance/<int:class_instance_id>')
@flask_login.login_required
def get_student_class_instance(class_instance_id):
    student_class_instances = StudentClassInstance.query.filter(StudentClassInstance.class_instance_id == class_instance_id).all()
    student_class_instances = to_json(student_class_instances)
    return student_class_instances

@app.route('/api/student_class_instance/<int:id>/<string:attendance>')
@flask_login.login_required
def update_student_class_instance_attendance(id, attendance):
    try:
        student_class_instance = StudentClassInstance.query.filter(StudentClassInstance.id == id).one()
        student_class_instance.attendance = attendance
        db.session.commit()
        result = to_json(student_class_instance)
        return result
    except NoResultFound:
        # TODO add some custom error message here
        pass


@app.route('/api/student_class_schedule')
@flask_login.login_required
def get_student_class_schedule():
    saturday_class = StudentClassSchedule.query.filter(StudentClassSchedule.class_schedule_id == 3).all()

    enrolled_students = to_json(saturday_class)

    return enrolled_students
