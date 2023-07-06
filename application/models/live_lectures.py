from aplication import db

class LiveLectures(db.Model):
    live_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer,db.ForeignKey('courses.course_id'))
    lecture_title = db.Column(db.String())
    lecture_description = db.Column(db.String(2000))

    status = db.Column(db.String(100))
    starting_time = db.Column(db.String(50))
    ending_time = db.Column(db.String(30))
    