from .database import connect_db
from server import app
from .Student.endpoint import get_students, get_student_class_instance, get_student_class_schedule
from .Coach.endpoint import get_coach
from .ClassSchedule.endpoint import get_class_schedule, get_class_instance
