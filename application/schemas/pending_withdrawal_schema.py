from application import ma

class PendingWithdrawalSchema(ma.Schema):
    class Meta:
        fields = ('p_withdrawal_id','bank_iban_number','is_paid','paid_date','email','full_name','total_amount')