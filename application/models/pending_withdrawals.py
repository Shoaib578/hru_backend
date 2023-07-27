from application import db
from datetime import datetime

class PendingWithdrawals(db.Model):
    p_withdrawal_id = db.Column(db.Integer,primary_key=True)
    bank_iban_number = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'))
    email = db.Column(db.String(255))
    full_name = db.Column(db.String(255))
    is_paid = db.Column(db.Boolean(),default=False)
    total_amount = db.Column(db.Integer())
    paid_date = db.Column(db.DateTime(),nullable=True)