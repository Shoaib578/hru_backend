from application import db


class Wallets(db.Model):
    wallet_id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.ForeignKey('users.user_id'))
    amount = db.Column(db.Integer())