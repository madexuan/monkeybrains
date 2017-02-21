from api.database import db


class ClassSchedule(db.Model):
    """tbd"""

    __tablename__ = "class_schedule"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=True)
    day_of_week = db.Column(db.String(9), nullable=False)
    time = db.Column(db.Time, nullable=False)
    coach_id = db.Column(db.Integer, db.ForeignKey('coach.id'), nullable=True)

    coach = db.relationship("Coach",
                            backref=db.backref("class_schedule", order_by=id))

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<ClassSchedule id={} day_of_week={} time={}>".format(self.id, self.day_of_week, self.time)


class ClassInstance(db.Model):
    """tbd"""

    __tablename__ = "class_instance"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_schedule_id = db.Column(db.Integer, db.ForeignKey('class_schedule.id'), nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.String(500), nullable=True)
    substitute_coach_id = db.Column(db.Integer, db.ForeignKey('coach.id'), nullable=True)

    # define a relationship to Coach
    substitute_coach = db.relationship("Coach",
                           backref=db.backref("substituted_classes", order_by=id))

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<ClassInstance id={} date={}>".format(self.id, self.date)
