from flask import Flask,Blueprint
from application.seeds.main import wallet

wallet_routes = Blueprint('wallet_routes', __name__,static_folder='../static')

@wallet_routes.route('/add_money_to_wallet',methods=['POST'])
def AddMoneyToWallet():
    return wallet.add_money_to_wallet()


@wallet_routes.route('/get_money_from_wallet')
def GetMoneyFromWallet():
    return wallet.get_money_from_wallet()



@wallet_routes.route('/create_transfer',methods=['POST'])
def CreateTransfer():
    return wallet.create_transfer()
