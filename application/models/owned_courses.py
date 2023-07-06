from application import db

class OwnedCourses(db.Model):
    owned_id = db.Column(db.Integer(),primary_key=True)
    owned_by = db.Column(db.Integer,db.ForeignKey('users.user_id'))
    course_id = db.Column(db.Integer,db.ForeignKey('courses.course_id'))