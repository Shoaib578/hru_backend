from flask import Blueprint
from application.seeds.panels.admin import pending_withdrawals

admin_pending_withdrawals_routes = Blueprint('admin_pending_withdrawals_routes',__name__)



@admin_pending_withdrawals_routes.route('/withdrawals/insert_withdrawal',methods=['POST'])
def InsertWithdrawal():
    return pending_withdrawals.insert_pending_withdraw()




@admin_pending_withdrawals_routes.route('/withdrawals/pay_withdrawal',methods=['POST'])
def PayWithdrawal():
    return pending_withdrawals.pay_withdrawal()



@admin_pending_withdrawals_routes.route('/withdrawals/get_all_withdrawals',methods=['GET'])
def GetAllWithdrawals():
    return pending_withdrawals.get_all_withdrawals()
