from application import db

class FeaturedCourses(db.Model):
    featured_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.ForeignKey('courses.course_id'))
    