from server import app
from api.Base.helper import to_json

from .model import Student, StudentClassInstance, StudentClassSchedule


@app.route('/student')
def get_students():
    ringo = Student.query.filter(Student.name_first == 'Ringo').one()
    return ringo.name_first


@app.route('/student_class_instance')
def get_student_class_instance():
    tardy_student = StudentClassInstance.query.filter(StudentClassInstance.attendance == 'T').one()
    return tardy_student.student.name_first


@app.route('/student_class_schedule')
def get_student_class_schedule():
    saturday_class = StudentClassSchedule.query.filter(StudentClassSchedule.class_schedule_id == 3).all()

    enrolled_students = to_json(saturday_class)

    return enrolled_students
