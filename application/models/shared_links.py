from application import db

class SharedLinks(db.Model):
    shared_link_id = db.Column(db.Integer,primary_key=True)
    link = db.Column(db.String(300))
    shared_by = db.Column(db.ForeignKey('users.user_id'))
    course_id = db.Column(db.ForeignKey('courses.course_id'))
