from application import db,app
from flask import request,jsonify
from application.models.coupons import Coupons
from application.schemas.coupon_schema import CouponSchema
def add_coupon():
    coupon_code = request.form.get('coupon_code')
    course_id = request.form.get('course_id')
    discount_percentage = request.form.get('discount_percentage')
    coupon = Coupons(course_id=course_id, discount_percentage=discount_percentage,coupon_code=coupon_code)
    db.session.add(coupon)
    db.session.commit()
    return jsonify({
        "status":"coupon added successfully",
        "is_added": True,
    })

def get_all_coupons():
    coupons_query = Coupons.query.all()
    coupon_schema = CouponSchema(many=True)
    coupons = coupon_schema.dump(coupons_query)
    return jsonify({
        "data":coupons
    })

def delete_coupon():
    coupon_id = request.form.get('coupon_id')
    coupon = Coupons.query.filter_by(coupon_id=coupon_id).first()
    db.session.delete(coupon)
    db.session.commit()
    return jsonify({
        "status":"coupon deleted successfully",
        "is_deleted": True,
    })