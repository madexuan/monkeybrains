from api.database import db


class Student(db.Model):
    """TODO"""

    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_first = db.Column(db.String(), nullable=True)
    name_last = db.Column(db.String(), nullable=True)
    rank_stripes = db.Column(db.Integer, nullable=True)
    rank_type = db.Column(db.String(), nullable=True)
    program = db.Column(db.String(), nullable=True)

    def __repr__(self):
        """<Student id=1 name=Bobby Fisher>"""
        return "<Student id={0} name={1}>".format(self.id, self.name_first + ' ' + self.name_last)


class StudentClassInstance(db.Model):
    """tbd"""

    __tablename__ = "student_class_instance"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    class_instance_id = db.Column(db.Integer, db.ForeignKey('class_instance.id'), nullable=False)
    attendance = db.Column(db.String(1), nullable=False)
    notes = db.Column(db.String, nullable=True)

    # define a relationship to Student
    student = db.relationship("Student",
                              backref=db.backref("student_class_instance", order_by=id))

    # define a relationship to ClassInstance
    class_instance = db.relationship("ClassInstance",
                                     backref=db.backref("student_class_instance", order_by=id))

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<StudentClassInstance id={} student_id = {} class_instance_id={} attendance={}>".format(self.id, self.student_id, self.class_instance_id, self.attendance)


class StudentClassSchedule(db.Model):
    """tbd"""

    __tablename__ = "student_class_schedule"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    class_schedule_id = db.Column(db.Integer, db.ForeignKey('class_schedule.id'), nullable=False)

    # define a relationship to Student
    student = db.relationship("Student",
                           backref=db.backref("student_class_schedule", order_by=id))

    # define a relationship to Class Schedule
    class_schedule = db.relationship("ClassSchedule",
                           backref=db.backref("student_class_schedule", order_by=id))

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<StudentClassSchedule student_id = {} class_schedule_id = {}>".format(self.student_id, self.class_schedule_id)
