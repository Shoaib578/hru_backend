from application.seeds.panels.admin import coupons
from flask import Blueprint

admin_coupon_routes = Blueprint('admin_coupon_routes',__name__)

@admin_coupon_routes.route('/add_coupon',methods=['POST'])
def Addcoupon():
    return coupons.add_coupon()


@admin_coupon_routes.route('/delete_coupon',methods=['DELETE'])
def DeleteCoupon():
    return coupons.delete_coupon()

@admin_coupon_routes.route('/get_all_coupons',methods=['GET'])
def GetAllCoupons():
    return coupons.get_all_coupons()