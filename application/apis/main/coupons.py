from application.seeds.main import coupons
from flask import Blueprint

main_coupon_routes = Blueprint('main_coupon_routes',__name__)

@main_coupon_routes.route('/find_coupon',methods=['GET'])
def Findcoupons():
    return coupons.find_coupon()