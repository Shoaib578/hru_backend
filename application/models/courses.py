from application import db
from datetime import datetime
class Courses(db.Model):
    course_id = db.Column(db.Integer,primary_key=True)
    course_title = db.Column(db.String(300))
    course_description = db.Column(db.String(2000))
    teacher_id = db.Column(db.ForeignKey('panel_users.panel_userid'))
    course_thumbnail = db.Column(db.String(200))
    course_price = db.Column(db.Integer())
    course_category = db.Column(db.String(100))
    created_at = db.Column(db.DateTime(),default=datetime.utcnow())
    updated_at = db.Column(db.DateTime(),onupdate=datetime.utcnow(),nullable=True)

    