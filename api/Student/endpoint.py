from server import app
from api.Base.helper import to_json

from .model import Student, StudentClassInstance, StudentClassSchedule


@app.route('/api/students')
def get_students():
    students = Student.query.all()
    students = to_json(students)
    return students


@app.route('/api/student_class_instance/<int:class_instance_id>')
def get_student_class_instance(class_instance_id):
    attendance = StudentClassInstance.query.filter(StudentClassInstance.class_instance_id == class_instance_id).all()
    attendance = to_json(attendance)
    return attendance


@app.route('/api/student_class_schedule')
def get_student_class_schedule():
    saturday_class = StudentClassSchedule.query.filter(StudentClassSchedule.class_schedule_id == 3).all()

    enrolled_students = to_json(saturday_class)

    return enrolled_students
