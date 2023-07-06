from flask import Blueprint
from application.seeds.panels.admin import account
admin_account_routes = Blueprint('admin_account_routes',__name__,static_folder='static')


@admin_account_routes.route('/update_admin_account',methods=['POST'])
def UpdateAdminAccount():
    return account.update_admin_account()


@admin_account_routes.route('/get_admin_details',methods=['GET'])
def GetAdminDetails():
    return account.get_admin_details()