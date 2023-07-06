from application.models.coupons import Coupons
from application.schemas.coupon_schema import CouponSchema
from flask import request,jsonify
def find_coupon():
    coupon_code = request.args.get('coupon_code')
    course_id = request.args.get('course_id')
    coupon_query = Coupons.query.filter_by(course_id=course_id,coupon_code=coupon_code).first()
    coupon_schema = CouponSchema(many=False)
    coupon = coupon_schema.dump(coupon_query)

    if coupon_query:
        return jsonify({
            "found":True,
            "data":coupon
        })
    else:
        return jsonify({
                    "found":False
                })