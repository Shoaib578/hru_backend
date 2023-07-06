from application import db
from datetime import datetime
class Lectures(db.Model):
    lecture_id = db.Column(db.Integer,primary_key=True)
    lecture_number = db.Column(db.Integer)
    lecture_title = db.Column(db.String(300))
    course_id = db.Column(db.Integer,db.ForeignKey('courses.course_id'))
    lecture_description = db.Column(db.String(2000))
    lecture_video = db.Column(db.String(200))
    lecture_type = db.Column(db.String(100))
    lecture_duration = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(),default=datetime.utcnow)
    