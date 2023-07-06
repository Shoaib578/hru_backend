from application import ma


class WalletSchema(ma.Schema):
    class Meta:
        fields = ('wallet_id','user_id','amount')