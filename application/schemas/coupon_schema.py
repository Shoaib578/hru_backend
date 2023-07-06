from application import ma

class CouponSchema(ma.Schema):
    class Meta:
        fields = ('coupon_code','coupon_id','course_id','discount_percentage')