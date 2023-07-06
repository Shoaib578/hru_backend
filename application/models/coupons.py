from application import db

class Coupons(db.Model):
    coupon_id = db.Column(db.Integer,primary_key=True)
    coupon_code = db.Column(db.String(100))
    course_id = db.Column(db.ForeignKey('courses.course_id'))
    discount_percentage = db.Column(db.Integer())
    