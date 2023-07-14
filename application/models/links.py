from application import db

class Links(db.Model):
    shared_link_id = db.Column(db.Integer,primary_key=True)
    link = db.Column(db.String(300))
    shared_by = db.Column(db.ForeignKey('users.user_id'))
    code = db.Column(db.String(100))
    course_id = db.Column(db.ForeignKey('courses.course_id'))
