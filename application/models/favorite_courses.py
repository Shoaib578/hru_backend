from application import db


class FavoriteCourses(db.Model):
    favorite_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.user_id'))
    course_id = db.Column(db.ForeignKey('courses.course_id'))