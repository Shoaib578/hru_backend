from application import db
from datetime import datetime
from application.models.pending_withdrawals import PendingWithdrawals
from application.models.wallets import Wallets
from application.schemas.pending_withdrawal_schema import PendingWithdrawalSchema
from flask import request,jsonify

def insert_pending_withdraw():
    bank_iban = request.form.get('bank_iban')
    full_name = request.form.get('full_name')
    email = request.form.get('email')
    total_amount = request.form.get('total_amount')
    user_id = request.form.get('user_id')
    new_widthdrawal = PendingWithdrawals(bank_iban_number=bank_iban, full_name=full_name, email=email,total_amount=total_amount,user_id=user_id)
    db.session.add(new_widthdrawal)

    wallet = Wallets.query.filter_by(user_id=user_id).first()
    wallet.amount = 0
    db.session.commit()
    return jsonify({
        "is_added":True,
        "status":"Successfully Sent Request.It may take 3-5 bussiness days to withdraw"
    })


def get_all_withdrawals():
    withdrawals= PendingWithdrawals.query.all()
    schema = PendingWithdrawalSchema(many=True)
    data = schema.dump(withdrawals)
    return jsonify({
        "data":data
    })




def pay_withdrawal():
    withdrawal_id = request.form.get('withdrawal_id')
    
    withdrawal = PendingWithdrawals.query.get(withdrawal_id)
    if withdrawal.is_paid == False:
        withdrawal.is_paid = True
        withdrawal.paid_date = datetime.utcnow()
        db.session.commit()
    return jsonify({
        "is_paid":True,
        "status":"It may take 3-5 bussiness days"
    })

